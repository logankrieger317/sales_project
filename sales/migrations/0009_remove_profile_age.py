# Generated by Django 4.2.7 on 2023-12-01 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0008_profile_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='age',
        ),
    ]
