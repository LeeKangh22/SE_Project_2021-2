from django.db import models

# Create your models here.
class Post(models.Model):
    M_id = models.CharField(max_length=20)
    M_pw = models.CharField(max_length=10)
    
    def __str__(self):
        return self.M_id
