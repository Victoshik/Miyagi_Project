# Generated by Django 4.0.2 on 2022-02-14 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miyagi_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='songs',
        ),
    ]