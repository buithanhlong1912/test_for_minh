# Generated by Django 3.1.3 on 2020-11-30 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dichvukham',
            name='bao_hiem',
            field=models.BooleanField(default=False),
        ),
    ]
