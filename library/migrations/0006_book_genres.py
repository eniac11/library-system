# Generated by Django 3.1.1 on 2020-09-30 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20200930_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(to='library.Genre'),
        ),
    ]
