# Generated by Django 4.2.3 on 2023-07-16 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_inventory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='item',
            new_name='item_id',
        ),
        migrations.AlterField(
            model_name='item',
            name='category_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='item_category', to='inventory.itemcategory'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='itemcategory',
            name='item_category_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
