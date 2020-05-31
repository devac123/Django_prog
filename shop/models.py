from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField
    product_name = models.CharField(max_length = 20)
    product_desc = models.CharField(max_length = 500)
    category = models.CharField(max_length= 50, default = "")
    sub_cetagery = models.CharField(max_length= 50, default= "")
    price = models.IntegerField( default=0)
    pub_date = models.DateField()
    img = models.ImageField(upload_to="shop/img",default="")
    def __str__(self):
        return self.product_name


myob = Product(models.Model)
print(myob)