from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class TraineeInfo(models.Model):
    GENDERS = [
        ('F', 'FEMALE'),
        ('M', 'MALE'),
        ('N', 'NEUTRAL'),
    ]
    GOALS = [
        ('WL', 'WEIGHT LOSE'),
        ('MG', 'MUSCLE GAIN'),
        ('DF', 'DEFINITION')
    ]
    trainee = models.OneToOneField(User,
                                   on_delete=models.CASCADE,
                                   primary_key=True)
    name = models.CharField(max_length=150, unique=True)
    updated_date = models.DateField(auto_now=True)
    age = models.PositiveIntegerField(default=0)
    weight = models.DecimalField(max_digits=4, decimal_places=1)
    height = models.DecimalField(max_digits=4, decimal_places=1)
    sex = models.CharField(max_length=1, choices=GENDERS, default='N')
    goal = models.CharField(max_length=2, choices=GOALS, default='WL')

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name


class Exercises(models.Model):
    GROUPS = [
        ('BACK', 'BACK'),
        ('CHEST', 'CHEST'),
        ('LEGS', 'LEGS'),
        ('BICEPS', 'BICEPS'),
        ('TRICEPS', 'TRICEPS'),
        ('SHOULDERS', 'SHOULDERS'),
        ('CARDIO', 'CARDIO'),
        ('ABS', 'ABS'),
    ]
    LEVEL_CHOICES = [
        (1, 'BEGGINER'),
        (2, 'ADVANCED'),
        (3, 'EXPERT')
    ]
    GENDERS = [
        ('F', 'FEMALE'),
        ('M', 'MALE'),
        ('B', 'BOTH')
    ]
    name = models.CharField(max_length=150, unique=True)
    guide_image = CloudinaryField('image', default='None')
    muscle_group = models.CharField(max_length=10, choices=GROUPS)
    youtube_link = models.CharField(max_length=200, unique=True,
                                    default='None')
    level = models.IntegerField(choices=LEVEL_CHOICES, default=1)
    calories_burnt = models.PositiveIntegerField(default=0)
    gender = models.CharField(max_length=1, choices=GENDERS, default='B')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'exercise: {self.name}'


class WorkoutLog(models.Model):
    identifier = models.CharField(max_length=50, unique=True)
    day = models.PositiveIntegerField(default=1)
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


class Diet(models.Model):
    created_date = models.DateField(auto_now_add=True)
    trainee = models.ForeignKey(TraineeInfo,
                                on_delete=models.CASCADE,
                                related_name='diet_log')
    calories = models.PositiveIntegerField(default=0)
    calories_ideal = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['trainee', '-created_date']

    def __str__(self):
        return f'This diet is for: {self.trainee}'

