# Generated by Django 3.2.6 on 2021-08-30 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20210830_1900'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Home_Care_Nursing_Service',
            new_name='Care_Nursing_Service',
        ),
        migrations.RenameModel(
            old_name='Home_Health_Aide_Service',
            new_name='Health_Aide_Service',
        ),
        migrations.RenameModel(
            old_name='Homemaking_Services_Service',
            new_name='Homemaking_Service',
        ),
        migrations.RenameModel(
            old_name='Independent_Living_Skills_Service',
            new_name='Indp_Living_Skills_Service',
        ),
        migrations.RenameModel(
            old_name='Interpretive_Services_Service',
            new_name='Interpretive_Service',
        ),
        migrations.RenameModel(
            old_name='Social_Services_Service',
            new_name='Social_Service',
        ),
    ]
