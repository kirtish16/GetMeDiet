from django.db import models

# Contact model
class Contact(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    msg = models.TextField()
    def __str__(self):
        return self.user_name

# Breakfast model
class Breakfast(models.Model):
    name = models.CharField(max_length=500)
    amount = models.PositiveIntegerField()
    calories = models.PositiveIntegerField()

# Lunch model
class Lunch(models.Model):
    name = models.CharField(max_length=500)
    amount = models.PositiveIntegerField()
    calories = models.PositiveIntegerField()

# Dinner model
class Dinner(models.Model):
    name = models.CharField(max_length=500)
    amount = models.PositiveIntegerField()
    calories = models.PositiveIntegerField()