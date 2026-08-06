from django.db import models

class ProductItem(models.Model):
    PRODUCT_TYPE = [
        ('E', 'ELECTRONIC'),
        ('C', 'CLOTHES'),
        ('H', 'HOUSEHOLD'),
    ]

    # All fields must be indented inside the class
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(default='')
    product_type = models.CharField(max_length=1, choices=PRODUCT_TYPE)

    def __str__(self):
        return self.name