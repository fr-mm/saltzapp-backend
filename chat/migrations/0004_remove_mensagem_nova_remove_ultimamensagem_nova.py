# Generated by Django 4.1.5 on 2023-01-22 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_ultimamensagem_nova'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensagem',
            name='nova',
        ),
        migrations.RemoveField(
            model_name='ultimamensagem',
            name='nova',
        ),
    ]
