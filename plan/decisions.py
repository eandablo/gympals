from .models import TraineeInfo, WorkoutLog, Exercises


class WorkoutMaker():
    days = [{
            'day':1,
            'groups': ['BACK', 'BICEPS'],}
            'day':2,
            'groups': ['CHEST', 'TRICEPS'],}
            'day':1,
            'groups': ['LEGS', 'SHOULDERS'],}
        ]
    groups = Exercises.objects.order_by('muscle_group').distinct('muscle_group')
    for group in groups:

    def write_groups(self):
        return groups
