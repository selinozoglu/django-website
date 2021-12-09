# Generated by Django 3.2.9 on 2021-12-08 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20211208_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='makale',
            name='year_in_school',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], default='FR', max_length=2),
        ),
    ]
