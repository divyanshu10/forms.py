# Generated by Django 2.0.1 on 2018-03-17 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_auto_20180317_2148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='profile_pics',
            new_name='profile_pic',
        ),
    ]
