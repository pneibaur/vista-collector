# Generated by Django 4.1.2 on 2022-10-21 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vistas_collector', '0005_flair_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('vista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vistas_collector.vista')),
            ],
        ),
    ]