# Generated by Django 5.0.4 on 2024-04-22 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flower',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]