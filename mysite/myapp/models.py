from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    post_body = models.TextField()

    def __str__(self):
        return self.title

class Customer(models.Model):
    customer_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.customer_id
    
class Myfriend(models.Model):
    name=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    address=models.TextField()
    email=models.EmailField()
    photo=models.ImageField(upload_to='photo')
    created=models.DateField()

    def __str__(self):
        return self.name

