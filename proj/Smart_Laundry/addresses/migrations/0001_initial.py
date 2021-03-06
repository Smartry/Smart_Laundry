# Generated by Django 3.2.3 on 2021-06-05 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10, null=True)),
                ('phone_number', models.CharField(max_length=13, null=True)),
                ('address', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('password', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=30, null=True)),
                ('identification', models.CharField(max_length=10, null=True)),
                ('mem_point', models.IntegerField(null=True)),
                ('sex', models.IntegerField(null=True)),
                ('WM_hour', models.IntegerField(null=True)),
                ('WM_minute', models.IntegerField(null=True)),
                ('WM_remain_time', models.CharField(max_length=10, null=True)),
                ('Locker_hour', models.IntegerField(null=True)),
                ('Locker_minute', models.IntegerField(null=True)),
                ('Locker_remain_time', models.CharField(max_length=10, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
