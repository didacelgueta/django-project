# Generated by Django 3.0.4 on 2020-04-13 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('translate', '0013_auto_20200413_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('translated_text', models.CharField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='translate',
            name='translated_text',
        ),
        migrations.AddField(
            model_name='translate',
            name='translation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='translate.Result'),
            preserve_default=False,
        ),
    ]
