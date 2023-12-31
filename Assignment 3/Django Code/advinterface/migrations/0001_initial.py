# Generated by Django 3.2.13 on 2023-11-26 23:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buff_id', models.CharField(max_length=7, unique=True)),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advinterface.major')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('credit_hours', models.IntegerField()),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advinterface.major')),
            ],
        ),
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('contact_information', models.CharField(max_length=255)),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advinterface.major')),
            ],
        ),
    ]
