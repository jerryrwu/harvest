# Generated by Django 2.1.7 on 2019-04-06 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torrents', '0025_downloadlocation_is_preferred'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torrentinfo',
            name='tracker_id',
            field=models.CharField(db_index=True, max_length=65536),
        ),
    ]
