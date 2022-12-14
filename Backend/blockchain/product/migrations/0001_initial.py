# Generated by Django 4.0.6 on 2022-07-22 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track_Repairs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200, null=True)),
                ('percent_work_done', models.FloatField()),
                ('details_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.order_details')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.order_items')),
            ],
        ),
        migrations.CreateModel(
            name='Shipping_Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('postal_code', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='NFT_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200, null=True)),
                ('expiry_date', models.DateTimeField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.order_items')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('total_amount', models.FloatField(default=0)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
