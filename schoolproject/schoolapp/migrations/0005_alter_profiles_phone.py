# Generated by Django 4.2.8 on 2023-12-15 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0004_rename_profile_profiles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='phone',
            field=models.TextField(),
        ),
    ]
