# Generated by Django 5.1.7 on 2025-04-14 16:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0004_alter_movie_synopsis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='register_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
