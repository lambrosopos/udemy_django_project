# Generated by Django 2.2.5 on 2020-01-23 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0002_auto_20200123_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profilePic',
            field=models.ImageField(blank=True, upload_to='profilePics'),
        ),
    ]
