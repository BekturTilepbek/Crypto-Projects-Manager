# Generated by Django 5.1.7 on 2025-03-22 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='links',
        ),
    ]
