# Generated by Django 3.0.5 on 2020-11-14 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='places',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cityname', models.CharField(max_length=30)),
                ('heading', models.CharField(max_length=30)),
                ('content', models.CharField(default='', max_length=300)),
                ('image', models.ImageField(upload_to='images')),
                ('location', models.CharField(max_length=30)),
            ],
        ),
    ]
