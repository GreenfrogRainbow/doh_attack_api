# Generated by Django 4.2 on 2024-05-31 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doh_attack', '0005_shapdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shapdata',
            name='Label_score',
        ),
    ]
