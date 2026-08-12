
from django.db import models






class Watch(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    screensize = models.DecimalField(max_digits=4, decimal_places=2)
    mechanism = models.CharField(max_length=100)
    water_resistant = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.brand} {self.model}"

    class Meta:
        verbose_name = "Watch"
        verbose_name_plural = "Watches"


        






