# Generated by Django 3.2.6 on 2021-08-19 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0012_alter_customtemplate_docfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='template',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='generator.customtemplate'),
        ),
    ]
