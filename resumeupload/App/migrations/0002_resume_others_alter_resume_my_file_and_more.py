# Generated by Django 4.1.7 on 2023-03-17 12:17

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='others',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='my_file',
            field=models.FileField(upload_to='doc'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='profile_image',
            field=models.ImageField(upload_to='profileimg'),
        ),
    ]
