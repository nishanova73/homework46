# Generated by Django 4.0 on 2022-01-03 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='create_until',
            field=models.DateField(auto_now_add=True, verbose_name='Create_until'),
        ),
    ]
