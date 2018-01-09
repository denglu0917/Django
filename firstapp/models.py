from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    belong_to = models.OneToOneField(
        to=User, related_name='profile', on_delete=models.CASCADE)
    profile_image = models.FileField(
        null=True, blank=True, upload_to='profile_image')


class Article(models.Model):
    title = models.CharField(null=True, blank=True, max_length=100)
    img = models.CharField(null=True, blank=True, max_length=200)
    img_cover = models.FileField(upload_to='cover_image', null=True)
    content = models.TextField(null=True, blank=True)
    views = models.IntegerField(null=True, blank=True)
    favs = models.IntegerField(null=True, blank=True)
    createtime = models.DateField(auto_now=True)
    editors_choice = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(null=True, blank=True, max_length=50)
    avatar = models.CharField(
        default='/static/images/default.png', max_length=200)
    content = models.TextField(null=True, blank=True)
    createtime = models.DateField(auto_now=True)
    belong_to = models.ForeignKey(
        to=Article,
        related_name='under_comment',
        null=True,
        blank=True,
        on_delete=models.CASCADE)
    best_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.name
