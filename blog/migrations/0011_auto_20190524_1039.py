# Generated by Django 2.1.7 on 2019-05-24 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20190523_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='latest',
            name='last_update',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
