# Generated by Django 2.2.15 on 2020-09-24 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0027_adsrightbanner'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdsTopBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='Place Your Ad', max_length=200)),
                ('image', models.ImageField(default=None, upload_to='banners/%Y/%m/%d')),
            ],
        ),
    ]