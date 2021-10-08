from django.db import models
from users.models import User
from datetime import datetime

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    thumb = models.ImageField(upload_to='thumb_courses')

    def __str__(self) -> str:
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    video = models.FileField(upload_to='classes')
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    comment = models.TextField()
    created_at = models.DateTimeField(default=datetime.now())
    lesson = models.ForeignKey(Lesson, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.user.name


class Rate(models.Model):
    choices = (
        ('1', 'Péssimo'),
        ('2', 'Ruim'),
        ('3', 'Regular'),
        ('4', 'Bom'),
        ('5', 'Ótimo')
    )

    lesson = models.ForeignKey(Lesson, on_delete=models.DO_NOTHING)
    rate = models.CharField(max_length=50, choices=choices)
    created_at = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.user.name
