# Generated by Django 3.2.7 on 2021-09-18 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0015_auto_20210918_2208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='year',
            new_name='category',
        ),
    ]