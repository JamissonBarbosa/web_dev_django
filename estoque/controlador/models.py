from django.db import models

# Create your models here.
class Prateleira(models.Model):
    product_name = models.CharField(max_length=50)
    product_describe = models.CharField(max_length=200)
    
    def  __str__(self):
        return self.product_name, self.product_describe