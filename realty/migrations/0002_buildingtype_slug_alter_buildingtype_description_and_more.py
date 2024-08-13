# Generated by Django 5.0.7 on 2024-08-06 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildingtype',
            name='slug',
            field=models.SlugField(default=None, max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='buildingtype',
            name='description',
            field=models.CharField(help_text='Описание', max_length=250),
        ),
        migrations.AlterField(
            model_name='buildingtype',
            name='name',
            field=models.CharField(help_text='Наименование', max_length=250),
        ),
    ]
