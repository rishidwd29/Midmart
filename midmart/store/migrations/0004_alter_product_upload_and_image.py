# Generated by Django 4.2.4 on 2023-08-14 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0003_remove_product_product_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="Upload_and_image",
            field=models.FileField(null=True, upload_to=""),
        ),
    ]
