# Generated by Django 4.2.16 on 2024-09-10 12:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('devicedata', '0002_thresholddata_climatecontroldata'),
    ]

    operations = [
        migrations.AddField(
            model_name='climatecontroldata',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='climatecontroldata',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='thresholddata',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thresholddata',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
