# Generated by Django 2.0.1 on 2018-01-09 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('img', models.CharField(blank=True, max_length=200, null=True)),
                ('context', models.TextField(blank=True, null=True)),
                ('views', models.IntegerField(blank=True, null=True)),
                ('favs', models.IntegerField(blank=True, null=True)),
                ('createtime', models.DateField()),
            ],
        ),
    ]
