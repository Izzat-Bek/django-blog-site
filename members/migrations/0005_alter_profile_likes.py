# Generated by Django 4.2.4 on 2024-01-24 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_alter_profile_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_profiles', to='members.profile', verbose_name='Likes'),
        ),
    ]
