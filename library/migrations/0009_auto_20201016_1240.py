# Generated by Django 3.1.2 on 2020-10-16 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_book_blurb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='blurb',
            field=models.TextField(default='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum', null=True),
        ),
    ]
