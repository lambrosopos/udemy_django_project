# Generated by Django 2.2.5 on 2020-01-17 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registering_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='password',
            field=models.CharField(default='password', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='members',
            name='verifyPassword',
            field=models.CharField(default='password', max_length=254),
            preserve_default=False,
        ),
    ]
