# Generated by Django 2.2.5 on 2020-01-23 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='portfolio_site',
            new_name='portfolioSite',
        ),
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='profile_pic',
            new_name='profilePic',
        ),
    ]
