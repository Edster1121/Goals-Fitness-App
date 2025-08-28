from django.shortcuts import render
from .models import Workout

def workout_list(request):
    workouts = Workout.objects
    return render(request, "app/index.html", {"workouts": workouts})