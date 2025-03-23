# Generated by Django 5.1.7 on 2025-03-22 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='priority',
            field=models.CharField(choices=[('Tier 1', 'Тир 1'), ('Tier 2', 'Тир 2'), ('Antifomo', 'Антифомо')], default='Antifomo', max_length=100, verbose_name='Приоритет'),
        ),
    ]
