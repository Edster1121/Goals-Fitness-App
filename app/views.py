from django.shortcuts import render
from .models import Workout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


def workout_list(request):
    workouts = Workout.objects
    return render(request, "app/index.html", {"workouts": workouts})

@login_required
def index(request):
    return render(request, "app/index.html")

def root_redirect(request):
    return redirect('login')