# Generated by Django 5.0 on 2023-12-28 15:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Profile', 'verbose_name_plural': 'Profiles'},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='url',
        ),
        migrations.AddField(
            model_name='profile',
            name='url_github',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='URL to github'),
        ),
        migrations.AddField(
            model_name='profile',
            name='url_instagram',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='URL to instagram'),
        ),
        migrations.AddField(
            model_name='profile',
            name='url_telegram',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='URL to telegram'),
        ),
        migrations.AddField(
            model_name='profile',
            name='url_website',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='URL to website'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile/Image'),
        ),
    ]
