# Generated by Django 3.2.5 on 2021-08-14 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('feed_time1', models.IntegerField()),
                ('feed_time2', models.IntegerField()),
                ('feed_time3', models.IntegerField()),
            ],
        ),
    ]
