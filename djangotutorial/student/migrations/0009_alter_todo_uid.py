# Generated by Django 5.2.3 on 2025-06-26 14:34

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_alter_todo_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('820b4116-46b7-4326-9ceb-0ad56f0536fb'), editable=False, primary_key=True, serialize=False),
        ),
    ]
