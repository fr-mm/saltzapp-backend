# Generated by Django 4.1.5 on 2023-01-22 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='whatsapp',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]