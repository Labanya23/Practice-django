from django.db import models

# Create your models here.

CATEGORY_CHOICES=(
    ('CL','Cold'),
    ('EY','Eye'),
    ('DT','Dehydration'),
    ('HT','Heatstock'),
    ('SA','Seasonal allergies'),
    ('TP','Typhoid'),
    ('OT','Other'),
    
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField(default='')
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.title

