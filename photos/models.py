from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length =30)
   
    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

class Category(models.Model):
    name = models.CharField(max_length =30)
   
    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

class Image(models.Model):
    name = models.CharField(max_length =60)
    description = models.TextField()
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image_path = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def my_images(self):
        all_images = Image.objects.all()
        return all_images 


    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(category__icontains=search_term)
        return images

    @classmethod
    def category_view(cls,category):
        categories = cls.objects.filter(categories=category)
        return categories

    @classmethod
    def location_view(cls,location):
        location = cls.objects.filter(location=location)
        return location


