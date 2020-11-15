from django.db import models
class streetfood(models.Model):
    citycode=models.AutoField
    cityname=models.CharField(max_length=30)
    heading=models.CharField(max_length=30)
    content=models.CharField(max_length=300,default="")
    image=models.ImageField(upload_to="images")
    location=models.CharField(max_length=30)
    def __str__(self):
        return self.cityname