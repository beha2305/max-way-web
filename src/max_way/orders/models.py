from django.db import models
class Orders(models.Model):
    user_id = models.IntegerField()
    address = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.address

class OrderItem(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product_id = models.IntegerField()
    count = models.SmallIntegerField()