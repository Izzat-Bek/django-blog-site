# Generated by Django 4.2.4 on 2024-02-27 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0014_alter_profile_follow'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['user__username'], 'verbose_name': 'Profile', 'verbose_name_plural': 'Profiles'},
        ),
    ]
