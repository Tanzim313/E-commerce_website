# Generated by Django 5.1.3 on 2024-12-13 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_orderplaced_payment_method_alter_customer_state_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Haryana', 'Haryana'), ('Punjab', 'Punjab'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Delhi', 'Delhi'), ('Tripura', 'Tripura'), ('Telangana', 'Telangana'), ('Assam', 'Assam'), ('Goa', 'Goa'), ('Bangladesh', 'Bangladesh'), ('Uttarakhand', 'Uttarakhand'), ('Rajasthan', 'Rajasthan'), ('Bihar', 'Bihar'), ('West Bengal', 'West Bengal'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Daman and Diu', 'Daman and Diu'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Chattisgarh', 'Chattisgarh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Puducherry', 'Puducherry'), ('Odisha', 'Odisha'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Chandigarh', 'Chandigarh'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Gujarat', 'Gujarat')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('GH', 'Ghee'), ('MS', 'Milkshake'), ('LS', 'Lassi'), ('CR', 'Curd'), ('ML', 'Milk'), ('IC', 'Ice-Creams'), ('CZ', 'Cheese'), ('PN', 'Paneer')], max_length=2),
        ),
    ]
