from django.db import models

class emp(models.Model):
    ename=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    salary=models.IntegerField()
    location=models.CharField(max_length=100)
    img=models.