from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=50, null=False, blank= False)
    category = models.ForeignKey(Category, on_delete= models.SET_NULL, null=True, blank=False)
    image = models.FileField(upload_to='images', null=True, blank=True)
    price = models.IntegerField(null=False, blank=False)
    detail = models.TextField()
    is_available = models.SmallIntegerField(choices=[(1, 'Have'), (2, "Don't have")], default=1)


    def __str__(self):
        return self.title