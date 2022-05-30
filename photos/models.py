from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length =50)

    def __str__(self):
        return self.name 

    @classmethod
    def save_category(self):
        self.save

    def delete_category(self):
        self.delete

class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
    
    @classmethod
    def update_location(cls,id,value):
        cls.objects.filter(id=id).update(image=value)

    
    def save_location(self):
        self.save

    def delete_location(self):
        self.delete

class Image(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    image_image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length =60)
    description = models.TextField()


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['category']
    @classmethod
    def category_search(cls,category):
        images=cls.objects.filter(category__icontains=category)
        return images

    def category_view(cls,category):
        category=cls.objects.filter(category=category)
        return category

    def location_view(cls,location):
        location =cls.objects.filter(location=location)
        return location

    def get_images(self):
        return Image.objects.all()

    def save_image(self):
        self.save

    def delete_image(self):
        self.delete