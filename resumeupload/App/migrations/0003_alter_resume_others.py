# Generated by Django 4.1.7 on 2023-03-17 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_resume_others_alter_resume_my_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='others',
            field=models.TextField(blank=True, null=True),
        ),
    ]
