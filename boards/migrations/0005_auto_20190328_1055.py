# Generated by Django 2.1.7 on 2019-03-28 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_auto_20190328_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='threadImg',
            field=models.FileField(upload_to='uploads/%Y/%m'),
        ),
    ]