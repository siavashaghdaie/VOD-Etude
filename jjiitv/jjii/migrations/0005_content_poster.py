# Generated by Django 3.2.16 on 2024-02-03 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jjii', '0004_rename_series_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='تصویر کوچک'),
        ),
    ]