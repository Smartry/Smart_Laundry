# Generated by Django 3.2.3 on 2021-06-06 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locker', '0002_remove_smartlocker_servo_motor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartlocker',
            name='is_locker_reserved',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
