from django.db import models

class Portfolio(models.Model):
    img_name = models.CharField(max_length=100)
    arts = models.ImageField(upload_to='images/')
