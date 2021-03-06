# Generated by Django 4.0.4 on 2022-05-17 10:58

import bibliotech.books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookauthor',
            name='photo',
            field=models.ImageField(upload_to=bibliotech.books.models.author_photos_path),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='logo',
            field=models.ImageField(upload_to=bibliotech.books.models.publisher_logos_path),
        ),
    ]
