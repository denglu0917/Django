from django.contrib import admin
from firstapp.models import Article, Comment, UserProfile, Ticket
# Register your models here.

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(UserProfile)
admin.site.register(Ticket)
