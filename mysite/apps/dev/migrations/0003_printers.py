# Generated by Django 3.0.6 on 2020-05-31 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dev', '0002_hardware_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Printers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_printers', models.CharField(max_length=200, verbose_name='Имя принтера')),
                ('IP', models.CharField(max_length=200, verbose_name='IP адрес')),
            ],
        ),
    ]