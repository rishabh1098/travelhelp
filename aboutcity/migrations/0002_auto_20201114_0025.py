# Generated by Django 3.0.5 on 2020-11-13 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutcity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutcity',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]