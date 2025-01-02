# Generated by Django 5.1.4 on 2025-01-02 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_alter_column_options_alter_task_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('In Progress', 'In Progress'), ('Done', 'Done')], default='Open', max_length=50),
        ),
    ]
