# Generated by Django 4.0.2 on 2022-02-05 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0011_alter_graphicards_rep'),
    ]

    operations = [
        migrations.AddField(
            model_name='graphicards',
            name='file_name',
            field=models.TextField(default='145'),
        ),
    ]
