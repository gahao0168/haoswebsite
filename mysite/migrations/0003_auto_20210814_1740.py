# Generated by Django 3.2.5 on 2021-08-14 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_feedtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedtime',
            name='feed_time2',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='feedtime',
            name='feed_time3',
            field=models.IntegerField(null=True),
        ),
    ]
