from django.db import models
from django.conf import settings

# Create your models here.
class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
	('Transport', 'Transport'),
	('Bills', 'Bills'),
	('Entertainment','Entertainment'),
	('Other', 'Other'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} spent {self.amount} on {self.category} on {self.date}"
    