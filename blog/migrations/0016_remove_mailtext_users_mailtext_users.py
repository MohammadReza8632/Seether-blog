# Generated by Django 4.0.10 on 2023-05-30 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_remove_mailtext_users_mailtext_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailtext',
            name='users',
        ),
        migrations.AddField(
            model_name='mailtext',
            name='users',
            field=models.ManyToManyField(to='blog.subscribers'),
        ),
    ]
