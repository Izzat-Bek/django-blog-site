# Generated by Django 4.2.4 on 2023-12-30 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_postmodel_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postmodel',
            old_name='conten11',
            new_name='content11',
        ),
    ]
