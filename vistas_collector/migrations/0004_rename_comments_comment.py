# Generated by Django 4.1.2 on 2022-10-19 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vistas_collector', '0003_comments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]