# Generated by Django 4.2.7 on 2023-12-01 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0007_remove_profile_position_profile_age_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='position',
            field=models.CharField(default='No Position', max_length=100),
        ),
    ]
