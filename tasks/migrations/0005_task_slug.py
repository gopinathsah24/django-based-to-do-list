# Generated by Django 3.0.4 on 2020-03-18 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_remove_task_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
