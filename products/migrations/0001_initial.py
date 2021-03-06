# Generated by Django 3.0.3 on 2020-04-23 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('icon_black_url', models.URLField(max_length=2000, null=True)),
                ('icon_active_url', models.URLField(max_length=2000, null=True)),
            ],
            options={
                'db_table': 'main_categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('short_description', models.CharField(blank=True, max_length=200, null=True)),
                ('unit_text', models.CharField(blank=True, max_length=50, null=True)),
                ('weight', models.CharField(blank=True, max_length=50, null=True)),
                ('origin', models.CharField(blank=True, max_length=300, null=True)),
                ('expiration_date', models.CharField(blank=True, max_length=500, null=True)),
                ('packing_type_text', models.CharField(blank=True, max_length=300, null=True)),
                ('delivery_time_type_text', models.CharField(blank=True, max_length=300, null=True)),
                ('original_price', models.IntegerField()),
                ('discount_percent', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('sales_index', models.IntegerField(default=0)),
                ('contactant', models.CharField(blank=True, max_length=500, null=True)),
                ('cart_image_url', models.URLField(blank=True, max_length=2000, null=True)),
                ('detail_image_url', models.URLField(blank=True, max_length=2000, null=True)),
                ('list_image_url', models.URLField(blank=True, max_length=2000, null=True)),
                ('incoming_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tags',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('thumbnail_url', models.URLField(blank=True, max_length=2000, null=True)),
                ('maincategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.MainCategory')),
            ],
            options={
                'db_table': 'sub_categories',
            },
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Product')),
                ('tag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Tag')),
            ],
            options={
                'db_table': 'products_tags',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.SubCategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(through='products.ProductTag', to='products.Tag'),
        ),
        migrations.CreateModel(
            name='DetailInfomation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_description', models.TextField(null=True)),
                ('product_image', models.TextField(null=True)),
                ('product_infomation', models.TextField(null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
            options={
                'db_table': 'detail_infomations',
            },
        ),
    ]
