# Generated by Django 3.0.6 on 2020-05-31 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='device_id',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
