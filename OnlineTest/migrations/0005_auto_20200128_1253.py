# Generated by Django 3.0.2 on 2020-01-28 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineTest', '0004_auto_20200128_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='test_id',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
