# Generated by Django 2.1.7 on 2019-04-05 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_latest_topic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='latest',
            options={'verbose_name': 'latest', 'verbose_name_plural': 'Entries'},
        ),
    ]
