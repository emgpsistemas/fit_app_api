from django.http import JsonResponse

from .models import Exercise, MuscleGroup


# Create your views here.
def muscle_group_list(request):
    muscle_groups = MuscleGroup.objects.all().values()
    return JsonResponse(list(muscle_groups), safe=False)


def exercises_list(request):
    exercises = Exercise.objects.all()
    data = {"exercises": list(exercises.values())}
    return JsonResponse(data)
