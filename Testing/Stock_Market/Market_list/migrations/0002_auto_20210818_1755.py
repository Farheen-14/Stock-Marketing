# Generated by Django 3.1.3 on 2021-08-18 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Market_list', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock_items',
            old_name='video_url',
            new_name='vurl',
        ),
    ]