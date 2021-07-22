from django.db import models

# Create your models here.
class Ebook(models.Model):
 title=models.CharField(max_length=100)
 price=models.FloatField()
 img_url=models.CharField(max_length=5000)

 def __str__ (self):
   return self.title

# book1 = Ebook()

class Cart_items(models.Model):
  title=models.CharField(max_length=100, null=True)
  price=models.FloatField(null=True)