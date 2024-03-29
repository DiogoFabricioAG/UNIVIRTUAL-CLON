# Generated by Django 5.0.2 on 2024-02-12 03:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0009_coursematerial_is_visible'),
        ('Quiz', '0004_quiz_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizproblem',
            name='solutions',
        ),
        migrations.AddField(
            model_name='quiz',
            name='solutions',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to='Course.course'),
        ),
    ]
