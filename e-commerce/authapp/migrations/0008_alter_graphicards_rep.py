# Generated by Django 4.0.2 on 2022-02-05 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0007_graphicards_delete_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graphicards',
            name='Rep',
            field=models.FilePathField(),
        ),
    ]
