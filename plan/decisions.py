from .models import TraineeInfo, WorkoutLog, Exercises
from django.shortcuts import get_object_or_404
import random


def workout_calories(name):
    logs = WorkoutLog.objects.filter(trainee__name=name, completed=False)
    total_calories = 0
    for log in logs:
        total_calories += log.excercise.calories_burnt

    return total_calories


class WorkoutGen:
    def select_ids(self, name):
        trainee = get_object_or_404(TraineeInfo, name=name)
        days = [{
                'day': 1,
                'groups': ['BACK', 'BICEPS']},
                {'day': 2,
                'groups': ['CHEST', 'TRICEPS']},
                # {'day':3,
                # 'groups': ['LEGS', 'SHOULDERS'],}
                ]
        for day in days:
            groups = day['groups']
            for group in groups:
                exercise_list = Exercises.objects.filter(muscle_group=group)
                ids = exercise_list.values_list('id')
                id_list = [x[0] for x in ids]
                random_list = random.sample(id_list, k=3)
                for id in random_list:
                    WorkoutLog.objects.create(
                        identifier='week1' + trainee.name + str(day['day']) +
                                   '-' + str(id),
                        day=day['day'],
                        trainee=trainee,
                        sets_ideal=3,
                        reps_ideal=12,
                        excercise=get_object_or_404(Exercises, id=id)
                    )

        return True


class DietGen:
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

        return calories


class SiteAnalysis():
    def total_trainees(self):
        trainees = TraineeInfo.objects.all()
        if trainees:
            n_trainees = trainees.count()
            total_age = 0
            for trainee in trainees:
                total_age += trainee.age
            average_age = total_age / n_trainees
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