# Generated by Django 3.1.2 on 2020-10-31 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_contactus'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactus',
            options={'verbose_name_plural': 'ContactUs'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': 'User'},
        ),
    ]