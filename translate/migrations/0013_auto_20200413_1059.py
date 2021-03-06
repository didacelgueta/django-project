# Generated by Django 3.0.4 on 2020-04-13 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translate', '0012_auto_20200413_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translate',
            name='lang_1',
            field=models.CharField(choices=[('en', 'English'), ('es', 'Spanish'), ('fr', 'French')], max_length=2, verbose_name='Source Language'),
        ),
        migrations.AlterField(
            model_name='translate',
            name='lang_2',
            field=models.CharField(choices=[('en', 'English'), ('es', 'Spanish'), ('fr', 'French')], max_length=2, verbose_name='Target Language'),
        ),
    ]
