# Generated by Django 3.2.7 on 2021-11-06 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_delete_multipleimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
    ]
