# Generated by Django 3.0.4 on 2020-03-11 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0008_auto_20200311_1504'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='userid',
            new_name='owner',
        ),
    ]