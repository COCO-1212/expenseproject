from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator

# Create your models here.
class Expense(models.Model):
    # categories should contain a list of tuples with one for database and one for human reading
    CATEGORIES = [
    ("Food and Dining", "Food and Dining"),
    ("Housing", "Housing"),
    ("Transportation", "Transportation"),
    ("Entertainment", "Entertainment"),
    ("Healthcare", "Healthcare"),
    ("Utilities", "Utilities"),
    ("Education", "Education"),
    ("Personal Care", "Personal Care"),
    ("Gifts and Donations", "Gifts and Donations"),
    ("Insurance", "Insurance"),
    ("Travel", "Travel"),
    ("Debt Payments", "Debt Payments"),
    ("Savings and Investments", "Savings and Investments"),
    ("Taxes", "Taxes"),
    ("Clothing and Accessories", "Clothing and Accessories"),
    ("Home Maintenance", "Home Maintenance"),
    ("Pets", "Pets"),
    ("Children's Expenses", "Children's Expenses"),
    ("Miscellaneous", "Miscellaneous"),
    ("Business Expenses", "Business Expenses"),
]
    # tracking expenses with fields for title, date, amount, category, and an optional description.
    title = models.CharField(max_length=40)
    date = models.DateField(default=timezone.now)
    amount = models.DecimalField(max_digits=100, decimal_places=2, validators=[MinValueValidator(0.01)])
    category = models.CharField(max_length=30, choices=CATEGORIES) 
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title