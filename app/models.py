from idlelib.debugobj_r import remote_object_tree_item

from django.contrib.auth.models import User
from django.db import models

class Workout(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workouts")

    def __str__(self):
        return f"{self.name}"

class Exercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name="exercises")
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Set(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="sets")
    reps = models.IntegerField()
    weight = models.FloatField()

    def __str__(self):
        return f"{self.exercise.name}: {self.reps} x {self.weight}"