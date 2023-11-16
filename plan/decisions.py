from .models import TraineeInfo, WorkoutLog, Exercises
from django.shortcuts import get_object_or_404
import random


def select_ids(name):
        trainee = get_object_or_404(TraineeInfo, name=name)
        days = [{
                'day':1,
                'groups': ['BACK', 'BICEPS']},
                {'day':2,
                'groups': ['CHEST', 'TRICEPS']},
                # {'day':3,
                # 'groups': ['LEGS', 'SHOULDERS'],}
            ]
        all_ids = []
        for day in days:
            groups = day['groups']
            for group in groups:
                exercise_list = Exercises.objects.filter(muscle_group=group)
                ids = exercise_list.values_list('id')
                id_list = [x[0] for x in ids]
                random_list = random.sample(id_list, k=3)
                for id in random_list:
                    WorkoutLog.objects.create(
                        identifier='week1' + trainee.name + str(day['day'])+ '-' + str(id),
                        day=day['day'],
                        trainee = trainee,
                        sets_ideal = 3,
                        reps_ideal = 12,
                        excercise = get_object_or_404(Exercises, id=id)
                    )
        return 'week1' + trainee.name + str(day['day'])
