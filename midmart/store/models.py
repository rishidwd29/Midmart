from django.db import models

# Create your models here.
condition_choice = [
    ('1', 'below average'),
    ('2', 'average'),
    ('3', 'good'),
    ('4', 'very good'),
    ('5', 'brand new'),
]
class product(models.Model):
    product_id = models.IntegerField(auto_created=True)
    Product_name = models.CharField(max_length= 50)
    Product_Description = models.CharField(max_length= 200)
    Produc_Condition = models.CharField(max_length = 10, 
                                    choices = condition_choice)
    Listing_date = models.DateField( auto_now=True)
    Upload_and_image = models.FileField()

