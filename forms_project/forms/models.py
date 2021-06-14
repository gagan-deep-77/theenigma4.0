from django.db import models


class User(models.Model):
    name = models.CharField(max_length=500)
    password = models.CharField(max_length=600)

    def __str__(self):
        return self.name

class Room(models.Model):
    room_name = models.CharField(max_length=500)
    room_password = models.CharField(max_length=500)
    url = models.CharField(max_length=1000)

    def __str__(self):
        return self.room_name

class Questions(models.Model):
    question = models.CharField(max_length=1000)
    room = models.CharField(max_length=500)

    def __str__(self):
        return self.question

class Options(models.Model):
    option = models.CharField(max_length=1000)
    question = models.CharField(max_length=1000)
    room_name = models.CharField(max_length=500,default="")
    votes = models.IntegerField()
    voted_by = models.CharField(max_length=1000,default="")
    def __str__(self):
        return self.option


class Voters(models.Model):
    name = models.CharField(max_length=500)
    option = models.CharField(max_length=1000)
    question = models.CharField(max_length=1000)
    room_name = models.CharField(max_length=500, default="")
    option_id = models.IntegerField(default=0)


    def __str__(self):
        return self.name