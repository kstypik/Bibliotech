# Generated by Django 4.0.4 on 2022-05-17 10:42

import bibliotech.books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_bookauthor_twitter_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(upload_to=bibliotech.books.models.book_covers_path),
        ),
    ]