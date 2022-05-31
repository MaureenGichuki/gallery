from django.test import TestCase
from .models import *
import datetime as dt

# Create your tests here.
class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.pizza= Image(name= 'Pizza', description ='foodcam', location ='Greece', category="Food")

        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.pizza,Image))

        # Testing Save Method Image 
    def test_save_method(self):
        self.pizza.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

        # Testing Delete Method
    def test_delete_method(self):
        self.pizza.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images)== 0)

class LocationTestClass(TestCase):

    def setUp(self):
        # Creating a new Location and saving it
        self.greece= Location(name = 'Greece')

    def test_instance(self):
        self.assertTrue(isinstance(self.greece,Location))

    def test_save_method(self):
        self.greece.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)

class CategoryTestClass(TestCase):
    # Creating a new Category and saving it

    def setUp(self):
        self.food= Category(name = 'Food')

    def test_instance(self):
        self.assertTrue(isinstance(self.greece,Category))

    def test_save_method(self):
        self.food.save_category
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)



