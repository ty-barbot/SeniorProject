# Generated by Django 3.1.6 on 2021-04-22 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210328_2101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('Arm', 'Arm'), ('Leg', 'Leg'), ('Cardio', 'Cardio')], max_length=50)),
                ('rep_type', models.CharField(choices=[('Sets', 'Sets')], max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('Non-binary', 'Non-binary'), ('Prefer not to say', 'Prefer not to say')], max_length=20),
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('completed', models.BooleanField()),
                ('date', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('Arm', 'Arm'), ('Leg', 'Leg'), ('Cardio', 'Cardio')], max_length=50)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('sets', models.CharField(max_length=50)),
                ('machine', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.machine')),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.profile')),
            ],
        ),
    ]
