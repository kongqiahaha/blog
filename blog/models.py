from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone


class Textz(models.Model):
    text_id = models.AutoField(primary_key=True)
    text_favourite = models.IntegerField(default=0)
    text_user = models.CharField(max_length=20)
    text_date = models.DateField(default=timezone.now)
    text_head = models.CharField(max_length=20)
    text_tt = models.TextField()
    text_jianjie = models.TextField()


class Unfavourable(models.Model):
    user_id = models.AutoField(primary_key=True)
    favourite = models.IntegerField(default=0)


class Person(User):
    class Meta:
        proxy=True
