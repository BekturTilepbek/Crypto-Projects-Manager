# Generated by Django 5.1.7 on 2025-03-22 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_project_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='links',
            field=models.TextField(blank=True, null=True, verbose_name='Ссылки'),
        ),
    ]
