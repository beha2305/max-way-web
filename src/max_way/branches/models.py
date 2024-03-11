from django.db import models

class Branches(models.Model):
    name = models.CharField(max_length=150, null= False, blank=False)
    address_name = models.CharField(max_length=200, null=False, blank=False)
    work_time = models.CharField(max_length=200, null=False, blank=False)
    phone_number = models.CharField(max_length= 13, null= False, blank= False)
    status = models.SmallIntegerField(choices=[(1, "Active"), (2, "Inactive")], default=1)

    def __str__(self):
        return self.name