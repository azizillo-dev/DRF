from django.db import models

DISPLAY_CHOICES = [
    ('hd', 'HD'),
    ('full_hd', 'Full HD'),
    ('4k', '4K'),
]



class Product(models.Model):
    model = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    display = models.CharField(max_length=20, choices=DISPLAY_CHOICES, default='hd')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name









































