# Generated by Django 5.0.3 on 2024-06-20 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('option_1', models.CharField(max_length=100)),
                ('option_2', models.CharField(max_length=100)),
                ('option_3', models.CharField(max_length=100)),
                ('option_4', models.CharField(max_length=100)),
                ('option_1_count', models.IntegerField(default=0)),
                ('option_2_count', models.IntegerField(default=0)),
                ('option_3_count', models.IntegerField(default=0)),
                ('option_4_count', models.IntegerField(default=0)),
            ],
        ),
    ]
