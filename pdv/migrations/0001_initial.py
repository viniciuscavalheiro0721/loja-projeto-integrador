# Generated by Django 4.1.2 on 2022-10-23 06:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("products", "0003_remove_products_id_alter_products_active_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="cupom",
            fields=[
                ("fecha_cupom", models.BooleanField(default=0)),
                (
                    "codigo_cupom",
                    models.CharField(
                        max_length=7, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("acrescimo", models.DecimalField(decimal_places=2, max_digits=9)),
                ("dt_cupom", models.DateTimeField()),
                ("preco_custo", models.DecimalField(decimal_places=2, max_digits=9)),
                ("preco", models.DecimalField(decimal_places=2, max_digits=9)),
                ("cancela_cupom", models.BooleanField(default=0)),
                ("desconto", models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name="forma_pgto",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("payment_type", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Pdv",
            fields=[
                ("code_pdv", models.IntegerField(default=0, max_length=3)),
                (
                    "id_pdv",
                    models.IntegerField(
                        default=0, max_length=3, primary_key=True, serialize=False
                    ),
                ),
                ("balance_pdv", models.FloatField(default=0, max_length=10)),
                ("active_pdv", models.BooleanField(default=0)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "id_user_pdv",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="item_cupom",
            fields=[
                (
                    "codigo_item",
                    models.CharField(
                        max_length=7, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("preco", models.DecimalField(decimal_places=2, max_digits=9)),
                ("limite_cliente", models.IntegerField(null=True)),
                ("qtd_item", models.FloatField(default=0, max_length=5)),
                (
                    "codigo_cupom",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pdv.cupom"
                    ),
                ),
                (
                    "codigo_int",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.products",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="cupom",
            name="codigo_pgto",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="pdv.forma_pgto"
            ),
        ),
        migrations.AddField(
            model_name="cupom",
            name="id_pdv",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="pdv.pdv"
            ),
        ),
    ]
