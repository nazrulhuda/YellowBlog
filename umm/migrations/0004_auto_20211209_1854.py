# Generated by Django 3.2.9 on 2021-12-09 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('umm', '0003_auto_20211113_1355'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='comment',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='address',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='post',
            name='appointment',
        ),
        migrations.RemoveField(
            model_name='post',
            name='car',
        ),
        migrations.RemoveField(
            model_name='post',
            name='license',
        ),
        migrations.RemoveField(
            model_name='post',
            name='mechanic',
        ),
        migrations.RemoveField(
            model_name='post',
            name='phone',
        ),
        migrations.DeleteModel(
            name='Mechanics',
        ),
    ]
