# Generated by Django 4.2.11 on 2024-04-30 03:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('en_name', models.CharField(default='', max_length=255, primary_key=True, serialize=False)),
                ('ru_name', models.CharField(default='', max_length=255)),
                ('description', models.CharField(blank=True, default='', max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.category')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.IntegerField(default=0)),
                ('user_name', models.CharField(default='', max_length=255)),
                ('phone', models.CharField(default='', max_length=255)),
                ('locate', models.CharField(default='', max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=255)),
                ('img_base', models.CharField(blank=True, default='', max_length=255)),
                ('img_hover', models.CharField(blank=True, default='', max_length=255)),
                ('img_details_1', models.CharField(blank=True, default='', max_length=255)),
                ('img_details_2', models.CharField(blank=True, default='', max_length=255)),
                ('tag', models.CharField(blank=True, default='', max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductColor',
            fields=[
                ('en_value', models.CharField(default='', max_length=255, primary_key=True, serialize=False)),
                ('ru_value', models.CharField(default='', max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductGroup',
            fields=[
                ('id', models.CharField(default='', max_length=255, primary_key=True, serialize=False)),
                ('description', models.CharField(default='', max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('value', models.CharField(default='', max_length=255, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingSession',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSKU',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('price', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
                ('size_attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.productsize')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='color_attribute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.productcolor'),
        ),
        migrations.AddField(
            model_name='product',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.productgroup'),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.orderdetails')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
                ('product_sku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.productsku')),
            ],
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='shopping_session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.shoppingsession'),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.product')),
                ('product_sku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.productsku')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='shopping_session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.shoppingsession'),
        ),
    ]
