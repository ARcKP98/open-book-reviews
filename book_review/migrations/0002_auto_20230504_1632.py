# Generated by Django 3.2.18 on 2023-05-04 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_review', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='book_id',
            new_name='book_name',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='user_id',
            new_name='username',
        ),
    ]
