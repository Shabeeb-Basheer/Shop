from django.db import models
from django.urls import reverse_lazy

# Create your models here.
class Contact(models.Model):   
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    message = models.TextField()

    def __str__(self): 
        return self.name

class Project(models.Model):
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse_lazy("web:project_detail", kwargs={"slug": self.slug})
    def __str__(self):      
        return self.name    

class Product(models.Model):
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse_lazy("web:product_details", kwargs={"slug": self.slug})
    def __str__(self):      
        return self.name
    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blogs/')
    date = models.DateTimeField(auto_now_add=True)
   
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse_lazy("web:blog_details", kwargs={"slug": self.slug})
    def __str__(self):      
        return self.title
    
class CustomerFeedback(models.Model):   
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='feedbacks/')
    designation = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self): 
        return self.name
    
class Client(models.Model):   
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='clients/')
   
    def __str__(self): 
        return self.name
    
class ProductEnquiry(models.Model):   
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField()

    def __str__(self): 
        return self.name

from django.db import models

# class UpdateStatus(models.Model):
#     year = models.IntegerField()  # Use IntegerField for easier arithmetic
#     showroom = models.CharField(max_length=100)
#     customer = models.CharField(max_length=100)

#     def __str__(self): 
#         return str(self.year)

#     def increment_year(self):
#         self.year += 1
#         self.save()

    