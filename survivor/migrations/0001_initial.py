# Generated by Django 3.2.8 on 2022-01-06 16:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survivor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(120)])),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=25)),
                ('latitude', models.FloatField(validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90)])),
                ('longitude', models.FloatField(validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)])),
                ('infected', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('food', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('meds', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('ammo', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('owner_survivor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='inventory', to='survivor.survivor')),
            ],
        ),
    ]
