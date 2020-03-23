# Generated by Django 3.0.4 on 2020-03-23 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunr', '0002_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='preview_url',
            field=models.TextField(default='[Song name]'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='title',
            field=models.CharField(default='what', max_length=100),
            preserve_default=False,
        ),
    ]
