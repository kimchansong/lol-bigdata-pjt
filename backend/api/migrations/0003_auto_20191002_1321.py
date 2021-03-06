# Generated by Django 2.2.4 on 2019-10-02 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_gameresult_item_data2'),
    ]

    operations = [
        # migrations.CreateModel(
        #     name='duodata',
        #     fields=[
        #         ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
        #         ('Bot1', models.CharField(max_length=30)),
        #         ('Bot2', models.CharField(max_length=30)),
        #         ('Play', models.CharField(max_length=30)),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='gameResult',
        #     fields=[
        #         ('id', models.IntegerField(primary_key=True, serialize=False)),
        #         ('userId', models.CharField(max_length=30)),
        #         ('line', models.CharField(max_length=30)),
        #         ('championId', models.CharField(max_length=30)),
        #         ('win', models.IntegerField()),
        #         ('kills', models.IntegerField()),
        #         ('death', models.IntegerField()),
        #         ('assists', models.IntegerField()),
        #     ],
        # ),
        migrations.CreateModel(
            name='item_data3',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('char_id', models.IntegerField(blank=True, default=0, null=True)),
                ('item_id', models.IntegerField(default=0, null=True)),
                ('item_cnt', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='item_data2',
        ),
    ]
