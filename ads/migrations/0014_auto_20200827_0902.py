# Generated by Django 2.2.15 on 2020-08-27 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0013_auto_20200826_2352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ads',
            name='category',
        ),
        migrations.AddField(
            model_name='ads',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ads.Category'),
        ),
    ]
