# Generated by Django 5.0.2 on 2024-02-22 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media_gallery', '0004_alter_pictures_description_alter_pictures_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pictures',
            name='description',
        ),
        migrations.RemoveField(
            model_name='pictures',
            name='title',
        ),
    ]
