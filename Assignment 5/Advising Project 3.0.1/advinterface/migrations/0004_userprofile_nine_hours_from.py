# Generated by Django 3.2.13 on 2023-12-03 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advinterface', '0003_auto_20231203_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='nine_hours_from',
            field=models.CharField(default='', max_length=255),
        ),
    ]
