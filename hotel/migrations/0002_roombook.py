# Generated by Django 3.1.2 on 2020-11-02 05:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roombook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival_date', models.DateField()),
                ('days', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=10)),
                ('number_of_guests', models.CharField(max_length=10)),
                ('notes', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roombook', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]