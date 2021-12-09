# Generated by Django 3.2.9 on 2021-12-07 14:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Makale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20, verbose_name='makalenin tipi')),
                ('text', models.TextField(verbose_name='içerik')),
                ('publish_date', models.DateField(default=django.utils.timezone.now, verbose_name='yayınlanma zamanı')),
                ('isVisible', models.BooleanField(verbose_name='makale yayınlansın mı')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
