# Generated by Django 4.0.4 on 2022-05-09 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_alter_makale_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='makale',
            name='description',
            field=models.CharField(default='makale açıklama', max_length=300, verbose_name='makale açıklama'),
        ),
        migrations.AlterField(
            model_name='makale',
            name='title',
            field=models.CharField(default='Baslık', max_length=200, verbose_name='makale başlık'),
        ),
    ]
