# Generated by Django 2.2 on 2019-05-01 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_remove_news_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
