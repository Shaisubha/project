# Generated by Django 3.2.4 on 2023-10-12 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField(max_length=10)),
                ('ename', models.CharField(max_length=100)),
                ('esal', models.FloatField()),
                ('eaddr', models.CharField(max_length=100)),
            ],
        ),
    ]
