# Generated by Django 3.2.3 on 2021-08-01 12:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_beatplay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beat',
            name='title',
            field=models.CharField(max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]