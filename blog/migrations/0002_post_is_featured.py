# Generated by Django 4.2.13 on 2024-05-26 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_featured',
            field=models.BooleanField(default=False, verbose_name='IS FEATURED'),
        ),
    ]
