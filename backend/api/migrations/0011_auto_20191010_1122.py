# Generated by Django 2.2.4 on 2019-10-10 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20191010_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='naivedata',
            name='all',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
