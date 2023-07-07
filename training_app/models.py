from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + " " + self.last_name


class MuscleGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    muscle_group = models.ForeignKey(MuscleGroup, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class WorkoutDuration(models.Model):
    workout_repetitions = models.IntegerField()

    def __str__(self):
        return self.duration


class Workout(models.Model):
    name = models.CharField(max_length=100)
    duration = models.ForeignKey(WorkoutDuration, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notes = models.TextField()
    number_of_series = models.IntegerField()
    number_of_repetitions = models.IntegerField()
    exercise = models.ForeignKey(
        Exercise, on_delete=models.SET_NULL, null=True, name="exercise"
    )

    def __str__(self):
        return self.name
