# Generated by Django 4.2.2 on 2023-06-17 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_version_num_of_version'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'permissions': [('set_published_product', 'Can publish product'), ('can_edit_description_and_category_product', 'Can edit description and category product')], 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
        migrations.AddField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='признак активности товара'),
        ),
    ]