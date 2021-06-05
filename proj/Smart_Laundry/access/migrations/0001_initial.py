# Generated by Django 3.2.3 on 2021-06-05 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessSystem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_access_door_open', models.BooleanField(default=False)),
                ('proximity_sensor', models.BooleanField(default=False)),
                ('locker', models.BooleanField(default=False)),
                ('servo_motor', models.BooleanField(default=False)),
                ('is_error_occurred', models.BooleanField(default=False)),
                ('error', models.CharField(max_length=20, null=True)),
                ('is_user_matched', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
