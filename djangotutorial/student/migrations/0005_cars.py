# Generated by Django 5.2.3 on 2025-06-17 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_alter_student_address_alter_student_age_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=100)),
                ('speed', models.IntegerField(default=50)),
            ],
        ),
    ]
