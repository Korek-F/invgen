# Generated by Django 3.2.6 on 2021-08-08 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitation',
            name='template',
            field=models.CharField(default='black', max_length=50),
            preserve_default=False,
        ),
    ]
