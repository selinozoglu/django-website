# Generated by Django 3.2.9 on 2021-12-08 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20211208_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='makale',
            name='title',
            field=models.CharField(default='Baslık', max_length=100, verbose_name='makale başlık'),
        ),
    ]
