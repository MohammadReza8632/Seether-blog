# Generated by Django 4.0.10 on 2023-06-01 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_mailmessage_delete_mailtext'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailmessage',
            name='users',
            field=models.ManyToManyField(to='blog.subscribers'),
        ),
    ]