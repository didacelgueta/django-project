# Generated by Django 3.0.4 on 2020-04-12 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translate', '0005_auto_20200411_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='translate',
            name='translated_text',
            field=models.CharField(default='NA', max_length=500),
            preserve_default=False,
        ),
    ]
