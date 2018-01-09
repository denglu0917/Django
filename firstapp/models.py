from django.db import models
# from faker import Factory
# Create your models here.


class Article(models.Model):
    title = models.CharField(null=True, blank=True, max_length=100)
    img = models.CharField(null=True, blank=True, max_length=200)
    content = models.TextField(null=True, blank=True)
    views = models.IntegerField(null=True, blank=True)
    favs = models.IntegerField(null=True, blank=True)
    createtime = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


# fake = Factory.create()
# for num in range(1):
#     v = Article(
#         title=fake.text(max_nb_chars=90),
#         content=fake.text(max_nb_chars=3000),
#     )
#     v.save()
