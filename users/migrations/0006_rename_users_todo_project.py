# Generated by Django 3.2.8 on 2022-09-28 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_project_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='users',
            new_name='project',
        ),
    ]