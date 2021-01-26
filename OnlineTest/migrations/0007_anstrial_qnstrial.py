# Generated by Django 3.0.2 on 2020-01-31 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineTest', '0006_test_marks'),
    ]

    operations = [
        migrations.CreateModel(
            name='QnsTrial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('keyword1', models.CharField(max_length=20)),
                ('keyword2', models.CharField(max_length=20)),
                ('keyword3', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='AnsTrial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answe', models.CharField(max_length=300)),
                ('keyword1', models.CharField(max_length=3)),
                ('keyword2', models.CharField(max_length=3)),
                ('keyword3', models.CharField(max_length=3)),
                ('qnstrial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OnlineTest.QnsTrial')),
            ],
        ),
    ]