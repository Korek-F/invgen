# Generated by Django 3.2.6 on 2021-08-11 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0007_invitation_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='template',
            field=models.CharField(choices=[('black', 'Black'), ('happy', 'Happy'), ('funny', 'Funny'), ('love', 'Love')], max_length=50),
        ),
    ]
