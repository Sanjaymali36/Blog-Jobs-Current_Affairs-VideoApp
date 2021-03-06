# Generated by Django 2.1.7 on 2019-03-22 05:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryWise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryWiseGK',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GK_Text', models.TextField(max_length=4000)),
                ('title', models.CharField(blank=True, max_length=200)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('link1', models.URLField(blank=True, null=True)),
                ('link2', models.URLField(blank=True, null=True)),
                ('link3', models.URLField(blank=True, null=True)),
                ('created_by', models.ForeignKey(default='BodhiAI', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts1', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=140)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Date_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='DateWiseGK',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GK_Text', models.TextField(max_length=4000)),
                ('title', models.CharField(blank=True, max_length=200)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('link1', models.URLField(blank=True, null=True)),
                ('link2', models.URLField(blank=True, null=True)),
                ('link3', models.URLField(blank=True, null=True)),
                ('created_by', models.ForeignKey(default='BodhiAI', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('Publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='gk_app.Date_Category')),
            ],
        ),
        migrations.CreateModel(
            name='TopicWise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('Publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics1', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics1', to='gk_app.CategoryWise')),
            ],
        ),
        migrations.AddField(
            model_name='datewisegk',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='gk_app.Topic'),
        ),
        migrations.AddField(
            model_name='categorywisegk',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts1', to='gk_app.TopicWise'),
        ),
    ]
