# Generated by Django 4.0.2 on 2022-02-10 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0014_alter_graphicards_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='graphicards',
            old_name='file_name',
            new_name='Reference',
        ),
    ]