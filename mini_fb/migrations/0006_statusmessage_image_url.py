# Generated by Django 4.0.3 on 2022-04-04 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0005_alter_statusmessage_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='statusmessage',
            name='image_url',
            field=models.URLField(blank=True),
        ),
    ]
