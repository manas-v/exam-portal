# Generated by Django 3.0.2 on 2020-01-27 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineTest', '0002_auto_20200127_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentlogindetails',
            name='studentdetails',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='OnlineTest.StudentDetails'),
        ),
        migrations.AlterField(
            model_name='studentsubjects',
            name='studentdetails',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='OnlineTest.StudentDetails'),
        ),
        migrations.AlterField(
            model_name='teachersubjects',
            name='teacherdetails',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='OnlineTest.TeacherDetails'),
        ),
    ]
