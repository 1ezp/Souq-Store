# Generated by Django 3.1.6 on 2021-02-19 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_accessories'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product_accessories',
            options={'verbose_name': 'Produect Accessory', 'verbose_name_plural': 'Product Accessories'},
        ),
        migrations.AlterModelOptions(
            name='product_alternative',
            options={'verbose_name': 'Produect Alternative', 'verbose_name_plural': 'Product Alternatives'},
        ),
        migrations.AlterField(
            model_name='category',
            name='CATDesc',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='category',
            name='CATImg',
            field=models.ImageField(upload_to='category/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='category',
            name='CATName',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='CATParent',
            field=models.ForeignKey(blank=True, limit_choices_to={'CATParent__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='Main Category'),
        ),
        migrations.AlterField(
            model_name='product_accessories',
            name='PACCAlternatives',
            field=models.ManyToManyField(related_name='product_Accessory', to='product.Product', verbose_name='Accessories'),
        ),
        migrations.AlterField(
            model_name='product_accessories',
            name='PACCProduct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mainAccessory_product', to='product.product', verbose_name='Produect'),
        ),
        migrations.AlterField(
            model_name='product_alternative',
            name='PALNAlternatives',
            field=models.ManyToManyField(related_name='product_alternative', to='product.Product', verbose_name='alternatives'),
        ),
        migrations.AlterField(
            model_name='product_alternative',
            name='PALNProduct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_product', to='product.product', verbose_name='Produect'),
        ),
    ]
