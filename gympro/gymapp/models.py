from django.db import models

# Create your models here.

class gymdatabase(models.Model):
    fname=models.CharField(max_length=200 ,null=False,blank=False)
    gender=models.CharField(max_length=30 ,null=False,blank=False)
    email=models.EmailField(max_length=200 ,null=False,blank=False)
    phone=models.CharField(max_length=55 ,null=False,blank=False)
    course=models.CharField(max_length=55 ,null=False,blank=False)
    room=models.CharField(max_length=55 ,null=False,blank=False)
    price=models.CharField(max_length=55 ,null=True,blank=False)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fname

    