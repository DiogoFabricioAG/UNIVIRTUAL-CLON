# Generated by Django 5.0.2 on 2024-02-07 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0003_course_asynchronous_course_requirements_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='code',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
