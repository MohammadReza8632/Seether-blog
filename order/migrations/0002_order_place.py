# Generated by Django 4.0.10 on 2023-07-23 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='place',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
