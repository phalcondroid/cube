# Generated by Django 4.0.5 on 2022-07-01 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cube', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shapeentity',
            name='number_side',
            field=models.IntegerField(),
        ),
    ]
