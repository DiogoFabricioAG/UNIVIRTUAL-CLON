# Generated by Django 5.0.2 on 2024-02-07 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0005_course_seccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='validation',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
