# Generated by Django 3.1.2 on 2020-12-31 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20201208_1510'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_day_and_fee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_day', models.CharField(max_length=10)),
                ('penalty', models.CharField(max_length=10)),
            ],
        ),
    ]