# Generated by Django 3.2.7 on 2021-09-07 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0018_auto_20210907_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply_now',
            name='cv',
            field=models.FileField(upload_to='Application-forms/cv/', verbose_name='CV'),
        ),
        migrations.AlterField(
            model_name='apply_now',
            name='signature',
            field=models.FileField(upload_to='Application-forms/signature/', verbose_name='Digital Signature'),
        ),
    ]