# Generated by Django 3.0.7 on 2020-06-11 08:12

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0008_auto_20200611_0811'),
    ]

    operations = [
        migrations.AddField(
            model_name='postdata',
            name='addmore',
            field=froala_editor.fields.FroalaField(default=''),
            preserve_default=False,
        ),
    ]
