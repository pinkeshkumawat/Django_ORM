# Generated by Django 3.2 on 2021-05-07 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('dept_id', models.IntegerField()),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_named', models.CharField(max_length=20)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app4_orm.student')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_name', models.CharField(max_length=20)),
                ('dep_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app4_orm.student')),
            ],
        ),
    ]
