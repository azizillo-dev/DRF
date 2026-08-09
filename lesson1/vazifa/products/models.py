from django.db import models



class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title



class Product(models.Model):
    title = models.CharField(max_length=120)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    desc = models.TextField()


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']


    









