# Generated by Django 2.2.15 on 2020-09-23 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0020_auto_20200922_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='profile_pic',
            field=models.ImageField(default='default-profile-pic.png', null=True, upload_to='uploads/profile-pictures'),
        ),
    ]