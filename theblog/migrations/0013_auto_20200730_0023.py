# Generated by Django 3.0.8 on 2020-07-30 07:23

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0012_auto_20200730_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, max_length=350, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.CharField(max_length=350),
        ),
    ]
