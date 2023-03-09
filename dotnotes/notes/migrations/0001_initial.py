# Generated by Django 4.0.5 on 2023-02-13 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('image', models.URLField()),
            ],
        ),
    ]
