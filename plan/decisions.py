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
        if sex == 'F':
            basal = 66.5 + 9.5634 * weight + 1.85 * height - 4.676 * age
        elif sex == 'M':
            basal = 66.5 + 13.75 * weight + 5.003 * height - 6.775 * age
        else:
            basal_m = 66.5 + 13.75 * weight + 5.003 * height - 6.775 * age
            basal_f = 66.5 + 9.5634 * weight + 1.85 * height - 4.676 * age
            basal = (basal_m + basal_f) * 0.5
        w_cal = workout_calories(name)
        if goal == 'WL':
            calories = 2.0 * basal
        elif goal == 'MG':
            calories = 2.5 * basal + w_cal
        else:
            calories = 2.0 * basal + w_cal

        return calories
