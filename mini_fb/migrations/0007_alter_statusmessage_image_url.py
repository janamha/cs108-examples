# Generated by Django 4.0.3 on 2022-04-04 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0006_statusmessage_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statusmessage',
            name='image_url',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
