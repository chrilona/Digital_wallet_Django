# Generated by Django 4.1 on 2022-09-09 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='profile_picture',
        ),
        migrations.AlterField(
            model_name='customer',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]