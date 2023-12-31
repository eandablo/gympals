from .models import TraineeInfo, WorkoutLog, Exercises
from django.shortcuts import get_object_or_404
import random


def insert_exercises_workout_plan(trainee, random_list, day):
    logs = WorkoutLog.objects.order_by(
        'created_date').filter(trainee=trainee, completed=True)
    if logs:
        last_log = logs.last()
        last_week = last_log.identifier
        num_position = last_week.find('-')
        if num_position == 5:
            week_number = int(last_week[num_position - 1]) + 1
        else:
            week_number = int(last_week[num_position - 2:num_position - 1]) + 1
    else:
        week_number = 1

    for id in random_list:
        # the workout plan is added here to WorkoutLog
        WorkoutLog.objects.create(
            identifier='week' + str(week_number) + '-' + str(id)
                       + trainee.name,
            day=day['day'],
            trainee=trainee,
            sets_ideal=3,
            reps_ideal=12,
            excercise=get_object_or_404(Exercises, id=id)
        )

    return ''


def choose_exercises_per_day(trainee, day):
    '''
    chooses exercises for a specific day
    accepts dictionary day as input variable
    '''
    groups = day['groups']
    for group in groups:
        if Exercises.objects.filter(muscle_group=group):
            exercise_list = Exercises.objects.filter(
                muscle_group=group)
            ids = exercise_list.values_list('id')
            id_list = [x[0] for x in ids]
            if len(id_list) > 2:
                random_list = random.sample(id_list, k=3)
            else:
                random_list = id_list

            insert_exercises_workout_plan(trainee, random_list, day)

    return ''


def workout_calories(name):
    '''
    function calculates total of calories expected to burn for
    a especific trainee due to workout
    '''
    logs = WorkoutLog.objects.filter(trainee__name=name, completed=False)
    total_calories = 0
    for log in logs:
        total_calories += log.excercise.calories_burnt

    return total_calories


class WorkoutGen:
    '''
    Creates a workout plan for a week for especific trainee
    '''

    def select_ids(self, name):
        trainee = get_object_or_404(TraineeInfo, name=name)
        days = [{
                'day': 1,
                'groups': ['BACK', 'BICEPS']},
                {'day': 2,
                'groups': ['CHEST', 'TRICEPS']},
                {'day': 3,
                'groups': ['LEGS', 'SHOULDERS']}
                ]
        # If there are exercises in the DB starts creating the plan
        if Exercises.objects.all():
            for day in days:
                choose_exercises_per_day(trainee, day)

        return ''


class DietGen:
    '''
    Calculates suggested calories for trainee depending on goal
    age, hight and weight
    logs the results in the TraineeInfo table
    '''

    def calories_calc(self, name):
        trainee = get_object_or_404(TraineeInfo, name=name)
        goal = trainee.goal
        sex = trainee.sex
        weight = float(trainee.weight)
        height = float(trainee.height)
        age = float(trainee.age)
        basal = 10 * weight + 3.0 * height - 5 * age
        if sex == 'F':
            basal -= 161
        elif sex == 'M':
            basal += 5.0
        else:
            basal -= 100
        w_cal = workout_calories(name)
        if goal == 'WL':
            calories = 1.85 * basal - 500
        elif goal == 'MG':
            calories = 2.2 * basal + w_cal
        else:
            calories = 1.85 * basal + w_cal
        trainee.calories = round(calories, 1)
        trainee.save()

        return ''


class SiteAnalysis:
    '''
    provides different functions for site analysis
    total_trainees calculates number of users and average age
    exercise_describe calculates total of exercises and muscle groups
    '''

    def total_trainees(self):
        trainees = TraineeInfo.objects.all()
        if trainees:
            n_trainees = trainees.count()
            total_age = 0
            for trainee in trainees:
                total_age += trainee.age
            average_age = round(total_age / n_trainees, 1)
        else:
            return False

        return [n_trainees, average_age]

    def exercises_describe(self):
        exercises = Exercises.objects.all()
        n_exercises = exercises.count()
        groups = exercises.order_by(
            'muscle_group').values_list('muscle_group').distinct()
        n_groups = len(groups)

        return [n_exercises, n_groups]

    def calc_performance(self):
        trainees = TraineeInfo.objects.all()
        total_performance = 1
        for trainee in trainees:
            logs = WorkoutLog.objects.filter(trainee=trainee, completed=True)
            factor = 0
            for log in logs:
                set_diff = (log.sets_ideal - log.sets_actual) / log.sets_ideal
                reps_diff = (log.reps_ideal - log.reps_actual) / log.reps_ideal
                factor += (1 - set_diff) * (1 - reps_diff)
            if logs:
                trainee_performance = factor / logs.count()
            else:
                trainee_performance = 1.0

            total_performance *= trainee_performance

        return round(total_performance, 2)
