# Generated by Django 2.2.4 on 2019-09-26 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='champion',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('key', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('blurb', models.CharField(max_length=300)),
                ('attack', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('magic', models.IntegerField()),
                ('difficulty', models.IntegerField()),
                ('tags', models.CharField(max_length=30)),
                ('partype', models.CharField(max_length=30)),
                ('hp', models.IntegerField()),
                ('hpperlevel', models.IntegerField()),
                ('mpperlevel', models.IntegerField()),
                ('movespeed', models.IntegerField()),
                ('armor', models.IntegerField()),
                ('armorperlevel', models.IntegerField()),
                ('spellblock', models.IntegerField()),
                ('spellblockperlevel', models.IntegerField()),
                ('attackrange', models.IntegerField()),
                ('hpregen', models.IntegerField()),
                ('hpregenperlevel', models.IntegerField()),
                ('mpregen', models.IntegerField()),
                ('mpregenperlevel', models.IntegerField()),
                ('crit', models.IntegerField()),
                ('critperlevel', models.IntegerField()),
                ('attackdamage', models.IntegerField()),
                ('attackdamageperlevel', models.IntegerField()),
                ('attackspeedperlevel', models.IntegerField()),
                ('attackspeed', models.IntegerField()),
            ],
        )
        # migrations.CreateModel(
        #     name='gameResult',
        #     fields=[
        #         ('id', models.IntegerField(primary_key=True, serialize=False)),
        #         ('userId', models.CharField(max_length=30)),
        #         ('championId', models.CharField(max_length=30)),
        #         ('win', models.IntegerField()),
        #         ('kills', models.IntegerField()),
        #         ('death', models.IntegerField()),
        #         ('assists', models.IntegerField()),
        #     ],
        # ),
    ]
