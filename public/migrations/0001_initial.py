# Generated by Django 3.0.4 on 2020-04-05 08:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('farmers', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='wishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('productid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='farmers.products')),
                ('userid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='userProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(default='', max_length=200)),
                ('house', models.CharField(default='', max_length=200)),
                ('town', models.CharField(default='', max_length=200)),
                ('pincode', models.CharField(default='', max_length=12)),
                ('phone', models.CharField(default='', max_length=12)),
                ('ismerchant', models.BooleanField(default=False)),
                ('description', models.CharField(default='', max_length=200)),
                ('img', models.ImageField(default='', upload_to='farmers/pics')),
                ('isactive', models.BooleanField(default=True)),
                ('license_no', models.CharField(default='', max_length=20)),
                ('manufacture_code', models.CharField(default='', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='orderDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('address', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('paymode', models.CharField(default=None, max_length=20)),
                ('productid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='farmers.products')),
                ('userid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('productid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='farmers.products')),
                ('userid', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
