# Generated by Django 3.0.2 on 2020-01-22 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='is_completed',
            new_name='completed',
        ),
    ]
