from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

<<<<<<< HEAD
=======

>>>>>>> 2c52029d933bfa5b243ae1059a6ec5ac632324c7
class KindOfSport(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    user = models.ManyToManyField(User)


class Inventory(models.Model):
    title = models.CharField(max_length=256)
    kindOfSport = models.ForeignKey(KindOfSport, on_delete=models.CASCADE)
    rating = models.IntegerField()
    user = models.ManyToManyField(User)


class Characteristic(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    key = models.CharField(max_length=256)
    meaning = models.CharField(max_length=256)


class Reviews(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    grade = models.IntegerField()
    message = models.CharField(max_length=256)
