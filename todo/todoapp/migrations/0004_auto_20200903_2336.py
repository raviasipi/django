# Generated by Django 3.1 on 2020-09-03 18:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_auto_20200831_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='create_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='target_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
