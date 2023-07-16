# Generated by Django 4.2.3 on 2023-07-12 02:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_itemcategory_item_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='item_category_id', to='inventory.itemcategory'),
        ),
    ]