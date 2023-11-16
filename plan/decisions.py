from .models import TraineeInfo, WorkoutLog, Exercises
import random


def select_ids():
        days = [{
                'day':1,
                'groups': ['BACK', 'BICEPS']},
                {'day':2,
                'groups': ['CHEST', 'TRICEPS']},
                # {'day':3,
                # 'groups': ['LEGS', 'SHOULDERS'],}
            ]
        # all_ids = []
        for day in days:
            groups = day['groups']
            for group in groups:
                exercise_list = Exercises.objects.filter(muscle_group=group)
                ids = exercise_list.values_list('id')
                id_list = [x[0] for x in ids]
                # random_list = random.sample(id_list, k=3)
        #         all_ids.extend(id_list)
        return id_list
