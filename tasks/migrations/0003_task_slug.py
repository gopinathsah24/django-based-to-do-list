# Generated by Django 3.0.4 on 2020-03-18 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20200123_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
