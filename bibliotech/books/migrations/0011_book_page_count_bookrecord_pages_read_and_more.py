# Generated by Django 4.0.4 on 2022-05-20 11:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_alter_book_genres'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='page_count',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(25000)]),
        ),
        migrations.AddField(
            model_name='bookrecord',
            name='pages_read',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(25000)]),
        ),
        migrations.AddConstraint(
            model_name='book',
            constraint=models.CheckConstraint(check=models.Q(('page_count__range', (1, 25000))), name='books_book_page_count_range'),
        ),
        migrations.AddConstraint(
            model_name='bookrecord',
            constraint=models.CheckConstraint(check=models.Q(('pages_read__range', (1, 25000))), name='books_bookrecord_pages_read_range'),
        ),
    ]
