# Generated by Django 4.0.10 on 2023-05-24 08:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_news_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
