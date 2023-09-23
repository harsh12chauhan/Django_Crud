from django.db import models

# Create your models here.
class userDetails(models.Model):
    name = models.CharField(max_length=150,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    password = models.CharField(max_length=200,null=True,blank=True)
    date_Time = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name
