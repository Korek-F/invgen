# Generated by Django 3.2.6 on 2021-08-07 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_from', models.CharField(max_length=40)),
                ('p_to', models.CharField(max_length=40)),
                ('place', models.CharField(max_length=60)),
                ('invitation_date', models.DateTimeField()),
                ('description', models.TextField()),
            ],
        ),
    ]
