# Generated by Django 4.0.1 on 2022-10-02 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('Food', 'Food'), ('Drinks', 'Drinks'), ('Готовая еда', 'Готовая еда'), ('Фрукты', 'Фрукты'), ('Овощи', 'Овощи'), ('Напитки', 'Напитки'), ('Кофе', 'Кофе')], max_length=40),
        ),
    ]