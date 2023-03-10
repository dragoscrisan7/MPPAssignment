from django.db import models


class Group(models.Model):
    groupNr = models.IntegerField(default=921)
    groupNickname = models.CharField(max_length=200, default='unknown name')
    language = models.CharField(max_length=200, default='romana')
    year = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.groupNickname


class Student(models.Model):
    firstname = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    favoriteNumber = models.IntegerField(default=0)
    favorite_colour = models.CharField(max_length=200, default='blue')
    GroupId = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Teacher(models.Model):
    firstname = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    TeachingSubject = models.CharField(max_length=200)
    years_of_experience = models.IntegerField(default=0)


