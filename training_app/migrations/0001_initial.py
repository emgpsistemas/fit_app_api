# Generated by Django 4.2.3 on 2023-07-06 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MuscleGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutDuration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workout_repetitions', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('notes', models.TextField()),
                ('number_of_series', models.IntegerField()),
                ('number_of_repetitions', models.IntegerField()),
                ('duration', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='training_app.workoutduration')),
                ('exercise', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='training_app.exercise')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training_app.user')),
            ],
        ),
        migrations.AddField(
            model_name='exercise',
            name='muscle_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='training_app.musclegroup'),
        ),
    ]