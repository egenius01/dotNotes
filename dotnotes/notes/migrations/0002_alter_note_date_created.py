# Generated by Django 4.0.5 on 2023-02-13 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]