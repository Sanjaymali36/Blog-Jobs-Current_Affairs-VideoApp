# Generated by Django 2.2 on 2019-06-17 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20190617_0708'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='hindi_news',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='news',
            name='title_hindi',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_text',
            field=models.TextField(blank=True),
        ),
    ]
