# Generated by Django 5.2.3 on 2025-06-14 14:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Product Name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('rating', models.FloatField(blank=True, default=0.0, null=True, verbose_name='Rating')),
                ('brand', models.CharField(max_length=100, verbose_name='Brand')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('available_colors', models.CharField(help_text='Separate colors with commas, e.g.: Red, Blue, Green', max_length=200, verbose_name='Available Colors')),
                ('image', models.ImageField(upload_to='products/', verbose_name='Product Image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Product Management',
            },
        ),
    ]
