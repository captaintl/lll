from django.db import models
# Create your models here.
class People(models.Model):
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=30)
    sex = models.BooleanField(default=True)
    phone = models.CharField(max_length=15)
    QQ = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    birth = models.CharField(max_length=30)
