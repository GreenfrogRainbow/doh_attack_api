# Generated by Django 4.2 on 2024-05-24 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doh_attack', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attackdata',
            name='banner',
            field=models.TextField(null=True),
        ),
    ]
