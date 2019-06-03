# Generated by Django 2.1.5 on 2019-05-23 11:25

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UpcomingEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organizer', models.CharField(max_length=50)),
                ('Date', models.DateField(blank=True, null=True)),
                ('starttime', models.TimeField(blank=True, null=True)),
                ('endtime', models.TimeField(null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('ticketprice', models.IntegerField(null=True)),
                ('slug', models.SlugField(blank=True, default='')),
            ],
        ),
    ]
