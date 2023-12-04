# Generated by Django 3.2.13 on 2023-12-03 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advinterface', '0004_userprofile_nine_hours_from'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='social_sciences',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='social_and_behavioral_sciences',
            field=models.ManyToManyField(related_name='social_sciences_courses', to='advinterface.Course'),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='advanced_cidm_electives',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='advanced_cidm_electives',
            field=models.ManyToManyField(related_name='advanced_cidm_electives_courses', to='advinterface.Course'),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='cis_requirements',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='cis_requirements',
            field=models.ManyToManyField(related_name='cis_requirements_courses', to='advinterface.Course'),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='component_area_option',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='component_area_option',
            field=models.ManyToManyField(related_name='component_area_option_courses', to='advinterface.Course'),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='mathematics',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='mathematics',
            field=models.ManyToManyField(related_name='mathematics_courses', to='advinterface.Course'),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='nine_hours_from',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='nine_hours_from',
            field=models.ManyToManyField(related_name='nine_hours_from_courses', to='advinterface.Course'),
        ),
    ]