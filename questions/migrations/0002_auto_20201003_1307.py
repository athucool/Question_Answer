# Generated by Django 3.1.1 on 2020-10-03 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ('-created_at',)},
        ),
    ]
