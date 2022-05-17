# Generated by Django 4.0.4 on 2022-05-17 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_genre_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(related_name='books', to='books.genre'),
        ),
    ]