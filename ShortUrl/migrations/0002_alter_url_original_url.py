# Generated by Django 3.2.10 on 2021-12-30 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShortUrl', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='original_url',
            field=models.URLField(help_text='Enter Url adress'),
        ),
    ]
