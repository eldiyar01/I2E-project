# Generated by Django 3.1.4 on 2020-12-13 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0009_auto_20201213_0321'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='scholarship',
            field=models.BooleanField(default=False),
        ),
    ]
