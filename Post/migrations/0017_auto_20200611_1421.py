# Generated by Django 3.0.7 on 2020-06-11 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0016_auto_20200611_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postdata',
            name='slug',
            field=models.SlugField(),
        ),
    ]
