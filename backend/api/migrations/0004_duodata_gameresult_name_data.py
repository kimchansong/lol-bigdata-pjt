# Generated by Django 2.2.4 on 2019-10-02 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20191002_1321'),
    ]

    operations = [
        migrations.CreateModel(
            name='duodata',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('Bot1', models.CharField(max_length=30)),
                ('Bot2', models.CharField(max_length=30)),
                ('Play', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='gameResult',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('userId', models.CharField(max_length=30)),
                ('line', models.CharField(max_length=30)),
                ('championId', models.CharField(max_length=30)),
                ('win', models.IntegerField()),
                ('kills', models.IntegerField()),
                ('death', models.IntegerField()),
                ('assists', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='name_data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item_id', models.IntegerField(default=0, null=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
