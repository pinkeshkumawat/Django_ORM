# Generated by Django 3.2 on 2021-05-10 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_orm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=30)),
                ('l_name', models.CharField(max_length=30)),
            ],
        ),
    ]
