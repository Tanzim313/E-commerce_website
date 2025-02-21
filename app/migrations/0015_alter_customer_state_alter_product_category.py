# Generated by Django 5.1.3 on 2024-12-18 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_rename_product_wishlist_product_alter_customer_state_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Assam', 'Assam'), ('Bangladesh', 'Bangladesh'), ('Telangana', 'Telangana'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Gujarat', 'Gujarat'), ('Tripura', 'Tripura'), ('Daman and Diu', 'Daman and Diu'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Tamil Nadu', 'Tamil Nadu'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Chattisgarh', 'Chattisgarh'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('West Bengal', 'West Bengal'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Bihar', 'Bihar'), ('Chandigarh', 'Chandigarh'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Delhi', 'Delhi'), ('Odisha', 'Odisha'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Punjab', 'Punjab'), ('Haryana', 'Haryana'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('Goa', 'Goa'), ('Puducherry', 'Puducherry')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('IC', 'Ice-Creams'), ('ML', 'Milk'), ('GH', 'Ghee'), ('CZ', 'Cheese'), ('CR', 'Curd'), ('MS', 'Milkshake'), ('LS', 'Lassi'), ('PN', 'Paneer')], max_length=2),
        ),
    ]
