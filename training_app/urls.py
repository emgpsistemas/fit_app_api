from django.urls import path

from . import views

urlpatterns = [
    path("muscle-groups/", views.muscle_group_list),
    path("exercises/", views.exercises_list),
]
