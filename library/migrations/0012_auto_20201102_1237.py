# Generated by Django 3.1.2 on 2020-11-02 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0011_series'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='series',
            name='books',
        ),
        migrations.AddField(
            model_name='series',
            name='books',
            field=models.ManyToManyField(to='library.Book'),
        ),
    ]
