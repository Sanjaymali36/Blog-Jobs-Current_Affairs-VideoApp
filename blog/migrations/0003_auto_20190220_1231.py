# Generated by Django 2.1.7 on 2019-02-20 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190220_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Blog_Text',
            field=models.TextField(),
        ),
    ]
