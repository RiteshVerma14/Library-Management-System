# Generated by Django 3.1.2 on 2020-12-03 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20201203_1336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='add_student_info',
            old_name='branch_name',
            new_name='course_name',
        ),
    ]
