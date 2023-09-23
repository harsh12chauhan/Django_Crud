from django.db import models

# Create your models here.
class details(models.Model):
    surname = models.CharField(max_length=50,blank=True,null=True)
    contact = models.BigIntegerField(blank=True,null=True)
    salary = models.IntegerField(blank=True,null=True)
    address = models.TextField(max_length=250,blank=True,null=True)
    date_Time = models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self):
        return self.surname
