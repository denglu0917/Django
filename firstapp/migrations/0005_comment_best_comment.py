# Generated by Django 2.0.1 on 2018-01-09 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_comment_belong_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='best_comment',
            field=models.BooleanField(default=False),
        ),
    ]
