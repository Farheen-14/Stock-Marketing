# Generated by Django 3.1.3 on 2021-08-18 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Market_list', '0003_auto_20210818_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
    ]
