from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils import timezone

class ProductItem(models.Model):
    PRODUCT_TYPE = [
        ('E', 'ELECTRONIC'),
        ('C', 'CLOTHES'),
        ('H', 'HOUSEHOLD'),
    ]

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(default='')
    product_type = models.CharField(max_length=1, choices=PRODUCT_TYPE)

    def __str__(self):
        return self.name


# ONE TO MANY (Reviews)

class ProductReview(models.Model):
    product = models.ForeignKey(ProductItem, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username}'s review on {self.product.name}"


# MANY TO MANY (Stores)

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    product_items = models.ManyToManyField(ProductItem, related_name='stores')

    def __str__(self):
        return self.name


# ONE TO ONE (Certificate)

class ProductCertification(models.Model):
    product = models.OneToOneField(ProductItem, on_delete=models.CASCADE, related_name='certificate')
    certificate = models.CharField(max_length=200)
    issued_date = models.DateField(default=timezone.now)
    valid = models.DateField()

    def __str__(self):
        return f"Certificate for {self.product.name}"
class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(
        max_length=50,
        default="fa-solid fa-notes-medical",
        help_text="Font Awesome class, e.g. fa-solid fa-heart"
    )
    slug = models.SlugField(unique=True, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

# from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone

# class ProductItem(models.Model):
#     PRODUCT_TYPE = [
#         ('E', 'ELECTRONIC'),
#         ('C', 'CLOTHES'),
#         ('H', 'HOUSEHOLD'),
#     ]

#     # All fields must be indented inside the class
#     name = models.CharField(max_length=50)
#     image = models.ImageField(upload_to='images/')
#     description = models.TextField(default='')
#     product_type = models.CharField(max_length=1, choices=PRODUCT_TYPE)

#     def __str__(self):
#         return self.name
    
#     #one to many
#     class ProductReview(models.Model):
#         product=models.ForeignKey(ProductItem, on_delete=models.CASCADE,related_name='review')
#         user=models.ForeignKey(User,on_delete=models.CASCADE)
#         rating=models.IntegerField()
#         comment=models.models.models.TextField()
#         date_added=models.DateTimeField(default=timezone.now)
    
#     #many to many
#     class Store(models.Model):
#         name=models.CharField(max_length=100)
#         location=models.CharField(max_length=100)
#         productItem=models.ManyToManyField(ProductItem,related_name='stores')
#     #one to one
#     class ProductCertification(models.Model):
#         product=models.OneToOneField(ProductItem,on_delete=models.CASCADE,related_name='certificate')
#         certificate=models.CharField(max_length=200)
#         issued_date=models.DateField(default=timezone.now)
#         valid=models.DateField()