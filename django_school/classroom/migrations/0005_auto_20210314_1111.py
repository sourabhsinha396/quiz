# Generated by Django 3.0.4 on 2021-03-14 05:41

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0004_auto_20200418_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
