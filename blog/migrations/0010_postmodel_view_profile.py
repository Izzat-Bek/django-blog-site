# Generated by Django 4.2.4 on 2024-02-04 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0011_profile_confidentiality'),
        ('blog', '0009_remove_starmodel_username_starmodel_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='view_profile',
            field=models.ManyToManyField(blank=True, related_name='post_view_user', to='members.profile', verbose_name='View'),
        ),
    ]
