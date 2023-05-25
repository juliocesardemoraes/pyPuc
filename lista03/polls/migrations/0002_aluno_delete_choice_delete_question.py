# Generated by Django 4.2.1 on 2023-05-25 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Aluno",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("idade", models.IntegerField()),
                ("endereco", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254)),
                ("telefone", models.CharField(max_length=20)),
                ("data_cadastro", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name="Choice",
        ),
        migrations.DeleteModel(
            name="Question",
        ),
    ]
