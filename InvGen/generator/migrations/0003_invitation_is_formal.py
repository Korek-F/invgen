# Generated by Django 3.2.6 on 2021-08-08 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0002_invitation_template'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitation',
            name='is_formal',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]