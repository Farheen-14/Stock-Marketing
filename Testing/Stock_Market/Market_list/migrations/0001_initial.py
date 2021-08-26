# Generated by Django 3.1.3 on 2021-08-18 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stock_items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('video', models.FileField(blank=True, null=True, upload_to='media')),
                ('video_url', models.URLField(max_length=300)),
            ],
        ),
    ]
