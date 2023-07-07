from django.contrib import admin

from .models import Exercise, MuscleGroup, User, Workout, WorkoutDuration

# Register your models here.

admin.site.register(MuscleGroup)
admin.site.register(Exercise)
admin.site.register(Workout)
admin.site.register(User)
admin.site.register(WorkoutDuration)
