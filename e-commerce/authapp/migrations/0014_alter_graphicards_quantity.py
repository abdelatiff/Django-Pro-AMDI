# Generated by Django 4.0.2 on 2022-02-07 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0013_alter_graphicards_file_name_alter_graphicards_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graphicards',
            name='Quantity',
            field=models.IntegerField(),
        ),
    ]
