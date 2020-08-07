# Generated by Django 3.0.6 on 2020-06-02 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0002_device_device_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='EndPoints',
            fields=[
                ('type', models.IntegerField(primary_key=True, serialize=False)),
                ('endpoint', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TargetUris',
            fields=[
                ('type', models.IntegerField(choices=[(1, 'Inverter'), (2, 'Scb'), (3, 'Em'), (4, 'Ws'), (5, 'Mfm')], primary_key=True, serialize=False)),
                ('uri', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='plant',
            name='interval',
            field=models.IntegerField(default=60),
        ),
    ]
