# Generated by Django 4.2.4 on 2024-01-24 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_profile_likes_starmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='user_likes', to='members.profile', verbose_name='Likes'),
        ),
    ]
