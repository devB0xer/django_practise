# Generated by Django 5.1.1 on 2024-09-12 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('someapp', '0002_author_bool_year'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bool',
            new_name='Book',
        ),
    ]
