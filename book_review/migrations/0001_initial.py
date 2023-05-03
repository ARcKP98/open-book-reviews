# Generated by Django 3.2.18 on 2023-05-03 14:50

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True)),
                ('author', models.CharField(max_length=300)),
                ('blurb', models.TextField()),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('approved', models.BooleanField(default=False)),
                ('image', cloudinary.models.CloudinaryField(default='Placeholder', max_length=255, verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField()),
                ('approved', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_for', to='book_review.book')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='book_genre', to='book_review.genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='like_count',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='book',
            name='uploaded_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_contributor', to=settings.AUTH_USER_MODEL),
        ),
    ]
