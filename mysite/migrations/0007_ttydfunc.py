# Generated by Django 3.2.5 on 2021-08-12 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_alter_func_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='TTYDFunc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
        ),
    ]
