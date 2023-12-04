# Generated by Django 3.2.13 on 2023-12-04 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advinterface', '0005_auto_20231203_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='advanced_cidm_electives',
            field=models.ManyToManyField(blank=True, related_name='advanced_cidm_electives_courses', to='advinterface.Course'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='cis_requirements',
            field=models.ManyToManyField(blank=True, related_name='cis_requirements_courses', to='advinterface.Course'),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='communication',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='communication',
            field=models.ManyToManyField(blank=True, related_name='communication_courses', to='advinterface.Course'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='component_area_option',
            field=models.ManyToManyField(blank=True, related_name='component_area_option_courses', to='advinterface.Course'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mathematics',
            field=models.ManyToManyField(blank=True, related_name='mathematics_courses', to='advinterface.Course'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nine_hours_from',
            field=models.ManyToManyField(blank=True, related_name='nine_hours_from_courses', to='advinterface.Course'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='social_and_behavioral_sciences',
            field=models.ManyToManyField(blank=True, related_name='social_sciences_courses', to='advinterface.Course'),
        ),
    ]
