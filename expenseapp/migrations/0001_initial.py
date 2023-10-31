# Generated by Django 4.2.6 on 2023-10-31 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=100)),
                ('category', models.CharField(choices=[('Food and Dining', 'Food and Dining'), ('Housing', 'Housing'), ('Transportation', 'Transportation'), ('Entertainment', 'Entertainment'), ('Healthcare', 'Healthcare'), ('Utilities', 'Utilities'), ('Education', 'Education'), ('Personal Care', 'Personal Care'), ('Gifts and Donations', 'Gifts and Donations'), ('Insurance', 'Insurance'), ('Travel', 'Travel'), ('Debt Payments', 'Debt Payments'), ('Savings and Investments', 'Savings and Investments'), ('Taxes', 'Taxes'), ('Clothing and Accessories', 'Clothing and Accessories'), ('Home Maintenance', 'Home Maintenance'), ('Pets', 'Pets'), ("Children's Expenses", "Children's Expenses"), ('Miscellaneous', 'Miscellaneous'), ('Business Expenses', 'Business Expenses')], max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
