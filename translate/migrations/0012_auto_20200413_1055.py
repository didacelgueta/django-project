# Generated by Django 3.0.4 on 2020-04-13 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translate', '0011_auto_20200413_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translate',
            name='lang_1',
            field=models.CharField(choices=[('en', 'English'), ('es', 'Spanish'), ('fr', 'French')], help_text='Select language', max_length=2, verbose_name='Language'),
        ),
    ]
