# Generated by Django 3.1.3 on 2020-11-06 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Hero',
            new_name='students',
        ),
    ]