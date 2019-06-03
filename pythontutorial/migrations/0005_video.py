# Generated by Django 2.1.5 on 2019-02-14 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pythontutorial', '0004_post_videoupload'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('videofile', models.FileField(null=True, upload_to='videos/', verbose_name='')),
                ('slug', models.SlugField(blank=True, default='')),
            ],
        ),
    ]
