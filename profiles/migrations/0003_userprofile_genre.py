# Generated by Django 3.0.2 on 2020-01-17 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20200118_0041'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='genre',
            field=models.CharField(max_length=255, null=True),
        ),
    ]