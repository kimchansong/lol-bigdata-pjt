# Generated by Django 2.2.4 on 2019-10-04 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20191002_1645'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pickban',
            fields=[
                ('char_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('char_name', models.CharField(max_length=30)),
                ('pickcount', models.IntegerField()),
                ('bancount', models.IntegerField()),
            ],
        ),
    ]
