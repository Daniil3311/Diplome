# Generated by Django 4.2.5 on 2023-10-19 18:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0003_alter_user_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="type",
            field=models.CharField(
                default="buyer", max_length=5, verbose_name="Тип пользователя"
            ),
        ),
    ]
