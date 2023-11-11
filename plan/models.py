from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


GROUPS = [
    ('BC', 'BACK'),
    ('CT', 'CHEST'),
    ('LG', 'LEGS'),
    ('BP', 'BICEPS'),
    ('TP', 'TRICEPS'),
    ('SH', 'SHOULDERS'),
]


class TraineeInfo(models.Model):
    trainee = models.OneToOneField(User,
                                   on_delete=models.CASCADE,
                                   primary_key=True)
    name = models.CharField(max_length=150, unique=True)
    updated_date = models.DateField(auto_now=True)
    age = models.PositiveIntegerField(default=0)
    weight = models.DecimalField(max_digits=4, decimal_places=1)
    height = models.DecimalField(max_digits=4, decimal_places=1)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name


class Exercises(models.Model):
    name = models.CharField(max_length=150, unique=True)
    guide_image = CloudinaryField('image', default='None')
    muscle_group = models.CharField(max_length=2, choices=GROUPS)
    youtube_link = models.CharField(max_length=200, unique=True,
                                    default='None')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'exercise: {self.name}'


class WorkoutLog(models.Model):
    identifier = models.CharField(max_length=50, unique=True)
    created_date = models.DateField(auto_now_add=True)
    trainee = models.ForeignKey(TraineeInfo,
                                on_delete=models.CASCADE,
                                related_name='workout_log')
    logged_date = models.DateField(auto_now=True)
    sets_ideal = models.PositiveIntegerField(default=0)
    sets_actual = models.PositiveIntegerField(default=0)
    reps_ideal = models.PositiveIntegerField(default=0)
    reps_actual = models.PositiveIntegerField(default=0)
    completed = models.BooleanField(default=False)
    excercise = models.ForeignKey(Exercises, on_delete=models.CASCADE,
                                  related_name='workout_exercise')

    class Meta:
        ordering = ['trainee', '-created_date']

    def __str__(self):
        return f'trainee: {self.trainee}'

# class SiteImages(models.Model):
#     role = models.CharField(max_length=100, primary_key=True)
#     image_url = CloudinaryField('image', default='add')
#     caption = models.TextField()
