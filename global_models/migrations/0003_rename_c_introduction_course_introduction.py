# Generated by Django 4.2.16 on 2024-09-30 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('global_models', '0002_course_credit_course_hours_course_place_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='C_introduction',
            new_name='introduction',
        ),
    ]