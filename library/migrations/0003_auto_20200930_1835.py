# Generated by Django 3.1.1 on 2020-09-30 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20200930_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.DateField(null=True),
        ),
    ]
