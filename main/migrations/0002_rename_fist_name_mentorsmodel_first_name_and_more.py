# Generated by Django 4.1.2 on 2022-10-14 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mentorsmodel',
            old_name='fist_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='studentsmodel',
            old_name='fist_name',
            new_name='first_name',
        ),
    ]