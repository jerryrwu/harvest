# Generated by Django 2.1.7 on 2019-04-01 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torrents', '0024_auto_20190327_0137'),
    ]

    operations = [
        migrations.AddField(
            model_name='downloadlocation',
            name='is_preferred',
            field=models.BooleanField(default=False),
        ),
    ]