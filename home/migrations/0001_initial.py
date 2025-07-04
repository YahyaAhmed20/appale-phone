# Generated by Django 5.2.3 on 2025-06-13 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('subtitle', models.CharField(blank=True, max_length=200, null=True, verbose_name='Subtitle')),
                ('image', models.ImageField(upload_to='carousel_images/', verbose_name='Image')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Content')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Order')),
            ],
            options={
                'verbose_name': 'Slide',
                'verbose_name_plural': 'Slides Management',
                'ordering': ['order'],
            },
        ),
    ]
