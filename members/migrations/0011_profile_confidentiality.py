# Generated by Django 4.2.4 on 2024-01-27 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0010_alter_starmodel_user_alter_starmodel_user_acc'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='confidentiality',
            field=models.BooleanField(default=True, verbose_name='Confidentiality'),
        ),
    ]
