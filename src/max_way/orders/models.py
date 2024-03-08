from django.db import models
from max_way.user.models import User
from max_way.product.models import Product
class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, null=False, blank=False)
    lat = models.CharField(max_length=200, null= True, blank=True)
    long = models.CharField(max_length=200, null= True, blank=True)

    def __str__(self):
        return self.address

class OrderItem(models.Model):
    oder = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.SmallIntegerField()
