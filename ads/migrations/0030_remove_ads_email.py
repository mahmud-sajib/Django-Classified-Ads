# Generated by Django 2.2.15 on 2020-09-25 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0029_adsbottombanner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ads',
            name='email',
        ),
    ]
