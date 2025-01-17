# Generated by Django 5.1.3 on 2024-12-14 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_payment_payer_id_payment_transaction_fee_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderplaced',
            old_name='Product',
            new_name='product',
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Daman and Diu', 'Daman and Diu'), ('Rajasthan', 'Rajasthan'), ('Delhi', 'Delhi'), ('Gujarat', 'Gujarat'), ('Assam', 'Assam'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Telangana', 'Telangana'), ('Chattisgarh', 'Chattisgarh'), ('Andhra Pradesh', 'Andhra Pradesh'), ('West Bengal', 'West Bengal'), ('Puducherry', 'Puducherry'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('Odisha', 'Odisha'), ('Tripura', 'Tripura'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Haryana', 'Haryana'), ('Goa', 'Goa'), ('Bihar', 'Bihar'), ('Bangladesh', 'Bangladesh'), ('Chandigarh', 'Chandigarh'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Punjab', 'Punjab'), ('Tamil Nadu', 'Tamil Nadu'), ('Sikkim', 'Sikkim')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('ML', 'Milk'), ('CZ', 'Cheese'), ('CR', 'Curd'), ('PN', 'Paneer'), ('IC', 'Ice-Creams'), ('GH', 'Ghee'), ('MS', 'Milkshake'), ('LS', 'Lassi')], max_length=2),
        ),
    ]
