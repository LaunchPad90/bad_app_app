# Generated by Django 3.0.3 on 2020-03-23 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='app',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.App'),
            preserve_default=False,
        ),
    ]