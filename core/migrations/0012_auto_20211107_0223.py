# Generated by Django 3.2.7 on 2021-11-06 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_post_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='images',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
