# Generated by Django 3.0.4 on 2020-03-11 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0006_auto_20200311_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='userid',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]