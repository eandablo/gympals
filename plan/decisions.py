from .models import TraineeInfo, WorkoutLog, Exercises
from django.shortcuts import get_object_or_404
import random


def workout_calories(name):
    logs = WorkoutLog.objects.filter(name=name, completed=False)
    total_cal = 0
    for log in logs:
        total_cal += log.excercise.calories_burnt

    return total_cal


class WorkoutGen():
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


class DietGen():
    def calories_calc(self, name):
        trainee = get_object_or_404(TraineeInfo, name=name)
        goal = trainee.goal
        sex = trainee.sex
        weight = trainee.weight
        height = trainee.height
        age = trainee.age
        if sex == 'F':
            basal = 66.5 + 9.5634 * weight + 1.85 * height - 4.676 * age
        elif sex == 'M':
            basal = 66.5 + 13.75 * weight + 5.003 * height - 6.775 * age
        else:
            basalM = 66.5 + 13.75 * weight + 5.003 * height - 6.775 * age
            basalF = 66.5 + 9.5634 * weight + 1.85 * height - 4.676 * age
            basal = (basalM + basalF) * 0.5
        if goal == 'WL':
            calories = basal
        elif goal == 'MG':
            calories == 1.5 * basal + 500
        else:
            calories = 1.2 * basal + 200
