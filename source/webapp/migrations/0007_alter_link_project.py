# Generated by Django 5.1.7 on 2025-03-22 16:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_link_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='webapp.project', verbose_name='Проект'),
        ),
    ]
