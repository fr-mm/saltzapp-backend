# Generated by Django 4.1.5 on 2023-01-18 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bot',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
    ]