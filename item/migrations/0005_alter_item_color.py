# Generated by Django 5.1.7 on 2025-04-02 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_item_date_added_item_date_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='color',
            field=models.CharField(choices=[('green', 'Green 🟩'), ('white', 'White ⬜'), ('blue', 'Blue 🟦')], max_length=10),
        ),
    ]
