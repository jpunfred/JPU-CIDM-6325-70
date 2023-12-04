# Generated by Django 3.2.13 on 2023-12-03 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advinterface', '0002_auto_20231203_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='advanced_cidm_electives',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='cis_requirements',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='communication',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='component_area_option',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='mathematics',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='social_sciences',
            field=models.CharField(default='', max_length=255),
        ),
    ]