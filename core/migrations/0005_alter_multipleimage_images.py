# Generated by Django 3.2.7 on 2021-10-25 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20211025_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multipleimage',
            name='images',
            field=models.FileField(upload_to='\\media'),
        ),
    ]
