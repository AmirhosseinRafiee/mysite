# Generated by Django 3.2.12 on 2022-04-20 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='approve',
            new_name='approved',
        ),
    ]
