# Generated by Django 3.0.2 on 2020-01-18 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_company_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='joined_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]