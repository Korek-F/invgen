# Generated by Django 3.2.6 on 2021-08-08 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0005_alter_invitation_invitation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='invitation_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
