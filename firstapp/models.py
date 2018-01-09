from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(null=True, blank=True, max_length=100)
    img = models.CharField(null=True, blank=True, max_length=200)
    context = models.TextField(null=True, blank=True)
    views = models.IntegerField(null=True, blank=True)
    favs = models.IntegerField(null=True, blank=True)
    createtime = models.DateField()

    def __str__(self):
        return self.title
