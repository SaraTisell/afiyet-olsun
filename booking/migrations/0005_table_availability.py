# Generated by Django 4.2.10 on 2024-02-18 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_alter_table_options_remove_table_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='availability',
            field=models.BooleanField(default=True),
        ),
    ]