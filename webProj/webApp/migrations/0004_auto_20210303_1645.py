# Generated by Django 3.1.7 on 2021-03-03 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0003_auto_20210302_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstories',
            name='story_date',
            field=models.DateField(blank=True, max_length=100, null=True),
        ),
    ]
