# Generated by Django 3.1.6 on 2021-02-11 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210211_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='productId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.products'),
        ),
    ]
