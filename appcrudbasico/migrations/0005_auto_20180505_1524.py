# Generated by Django 2.0.5 on 2018-05-05 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcrudbasico', '0004_auto_20180505_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
