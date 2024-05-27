# Generated by Django 4.2.13 on 2024-05-27 02:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
    ]