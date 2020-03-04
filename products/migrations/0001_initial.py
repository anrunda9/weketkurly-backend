# Generated by Django 3.0.2 on 2020-03-04 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_auto_20200229_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('icon_black_url', models.URLField(max_length=2000)),
                ('icon_active_url', models.URLField(max_length=2000)),
            ],
            options={
                'db_table': 'main_categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('unit_text', models.CharField(max_length=10)),
                ('weight', models.CharField(max_length=10)),
                ('origin', models.CharField(max_length=50)),
                ('contactant', models.CharField(max_length=300)),
                ('expiration_date', models.CharField(max_length=100)),
                ('packing_type_text', models.CharField(max_length=50)),
                ('original_price', models.IntegerField()),
                ('discount_percent', models.IntegerField()),
                ('original_image_url', models.URLField(max_length=2000)),
                ('main_image_url', models.URLField(max_length=2000)),
                ('list_image_url', models.URLField(max_length=2000)),
                ('short_description', models.CharField(max_length=200)),
                ('sticker_image_url', models.URLField(max_length=2000)),
                ('detail_image_url', models.URLField(max_length=2000)),
                ('stocks', models.IntegerField()),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='SpecialCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'special_categories',
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
                ('main_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.MainCategory')),
            ],
            options={
                'db_table': 'sub_categories',
            },
        ),
        migrations.CreateModel(
            name='SpecialCategoryProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Product')),
                ('special_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.SpecialCategory')),
            ],
            options={
                'db_table': 'special_categories_products',
            },
        ),
        migrations.AddField(
            model_name='specialcategory',
            name='product',
            field=models.ManyToManyField(through='products.SpecialCategoryProduct', to='products.Product'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_no', models.IntegerField()),
                ('review_title', models.CharField(max_length=100)),
                ('review_contents', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='users.User')),
            ],
            options={
                'db_table': 'reviews',
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
                ('product_description', models.TextField()),
                ('product_image', models.TextField()),
                ('product_infomation', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
            options={
                'db_table': 'detail_infomations',
            },
        ),
    ]
