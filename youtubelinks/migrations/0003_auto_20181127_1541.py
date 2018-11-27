# Generated by Django 2.1.3 on 2018-11-27 15:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('youtubelinks', '0002_auto_20181127_1358'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='youtubelink',
            options={'ordering': ('-timestamp',)},
        ),
        migrations.AddField(
            model_name='youtubelink',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
