# Generated by Django 4.2 on 2024-05-31 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doh_attack', '0006_remove_shapdata_label_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='flowdata',
            name='SourcePortPre',
            field=models.CharField(default=43, max_length=255),
            preserve_default=False,
        ),
    ]
