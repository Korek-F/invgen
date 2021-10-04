# Generated by Django 3.2.6 on 2021-08-18 10:04

from django.db import migrations, models
import generator.validators


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0011_auto_20210818_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customtemplate',
            name='docfile',
            field=models.FileField(upload_to='user_templates/%Y/%m/%d', validators=[generator.validators.validate_file_extension]),
        ),
    ]