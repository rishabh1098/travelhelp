from django.db import models
class aboutcity(models.Model):
    citycode=models.AutoField
    cityname=models.CharField(max_length=30)
    info=models.CharField(max_length=30)
    content=models.CharField(max_length=300,default="")
    image=models.ImageField(upload_to="images")
    def __str__(self):
        return self.cityname