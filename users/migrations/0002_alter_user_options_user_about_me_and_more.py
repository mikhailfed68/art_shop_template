# Generated by Django 4.1.7 on 2023-03-23 11:18

from django.db import migrations, models
import sorl.thumbnail.fields
import users.models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={"verbose_name": "user", "verbose_name_plural": "users"},
        ),
        migrations.AddField(
            model_name="user",
            name="about_me",
            field=models.CharField(
                blank=True, max_length=60, null=True, verbose_name="О себе"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="profile_picture",
            field=sorl.thumbnail.fields.ImageField(
                blank=True,
                null=True,
                upload_to=users.models.get_user_directory_path,
                verbose_name="Фото пользователя",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                error_messages={"unique": "Электронная почта уже используется."},
                help_text="Почта должна быть уникальной.",
                max_length=254,
                unique=True,
                verbose_name="Электронный адрес",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(
                help_text="\n        Обязательное поле. Не более 10 символов.\n        только буквы, цифры и символы @/./+/-/_.\n        ",
                max_length=10,
                unique=True,
                verbose_name="Имя пользователя",
            ),
        ),
    ]
