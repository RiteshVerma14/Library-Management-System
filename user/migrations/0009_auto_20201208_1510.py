# Generated by Django 3.1.2 on 2020-12-08 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_remove_add_student_info_branch_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_student_info',
            name='course_name',
        ),
        migrations.AddField(
            model_name='add_student_info',
            name='st_branch',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='add_student_info',
            name='st_course',
            field=models.CharField(default='', max_length=50),
        ),
    ]
