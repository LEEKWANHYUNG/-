from django.db import models


# Create your models here.
class Post(models.Model):
     Name = models.CharField(max_length = 200)
     date = models.DateTimeField('date published')
     body = models.TextField()
     writer = models.CharField(max_length = 200)
 
     def __str__(self):
         return self.Name

     def summary(self):
        return self.body[:100]
