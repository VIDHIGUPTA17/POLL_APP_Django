# Generated by Django 5.0.3 on 2024-06-20 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
