from django.db import models
from django.utils import timezone
# Create your models here.


class News(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    # pub_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title


class SportNews(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Register(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.username


