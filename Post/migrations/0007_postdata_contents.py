# Generated by Django 3.0.7 on 2020-06-11 08:09

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0006_auto_20200611_0701'),
    ]

    operations = [
        migrations.AddField(
            model_name='postdata',
            name='contents',
            field=froala_editor.fields.FroalaField(default=''),
            preserve_default=False,
        ),
    ]
