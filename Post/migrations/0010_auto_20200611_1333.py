# Generated by Django 3.0.7 on 2020-06-11 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0009_postdata_addmore'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postdata',
            options={'get_latest_by': 'published_date'},
        ),
        migrations.RemoveField(
            model_name='postdata',
            name='addmore',
        ),
        migrations.AddField(
            model_name='postdata',
            name='published',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='postdata',
            name='slug',
            field=models.SlugField(),
        ),
    ]
