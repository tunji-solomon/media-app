# Generated by Django 5.0.2 on 2024-03-05 13:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media_gallery', '0005_remove_pictures_description_remove_pictures_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=100)),
                ('video_file', models.FileField(upload_to='video')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media_gallery.gallery')),
            ],
        ),
    ]