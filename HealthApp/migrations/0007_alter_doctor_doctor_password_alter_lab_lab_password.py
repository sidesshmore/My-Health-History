# Generated by Django 4.2 on 2023-08-29 14:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("HealthApp", "0006_alter_doctor_doctor_password_alter_lab_lab_password"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctor",
            name="doctor_password",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="lab",
            name="lab_password",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
