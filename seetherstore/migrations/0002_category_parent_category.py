# Generated by Django 4.0.10 on 2023-07-05 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seetherstore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub_categories', to='seetherstore.category'),
        ),
    ]
