# Generated by Django 3.1.3 on 2020-11-29 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_auto_20201129_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.IntegerField(choices=[(1, 'female'), (2, 'male'), (3, 'others')], default=1),
        ),
    ]
