# Generated by Django 2.1.7 on 2019-03-03 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torrents', '0015_torrentinfo_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='torrent',
            name='status',
            field=models.IntegerField(choices=[(0, 'Check Waiting'), (1, 'Checking'), (2, 'Downloading'), (3, 'Seeding'), (4, 'Stopped')], default=0),
            preserve_default=False,
        ),
    ]
