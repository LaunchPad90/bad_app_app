# Generated by Django 3.0.3 on 2020-03-26 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='value',
            field=models.IntegerField(choices=[(1, 'GOOD'), (-1, 'BAD')]),
        ),
    ]