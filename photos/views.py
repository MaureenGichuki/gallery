from django.http  import HttpResponse,Http404
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render,redirect
from .models import Image, Location, Category

# Create your views here.
def home(request):

    images=Image.objects.all()
    location=Location.objects.all()
    category=Category.objects.all()

    if 'location' in request.GET and request.GET["location"]:
            location = request.GET.get("location")
            images = Image.location_view(location)

    else:
        if 'category' in request.GET and request.GET["category"]:

            category = request.GET.get("category")
            images = Image.category_view(category)

            return render(request, 'allphotos/display.html',{"image":images, "category":category, "location":location})

        return render(request, 'allphotos/display.html',{"image":images, "category":category, "location":location})


def search_results(request):
        
        if 'image' in request.GET and request.GET["image"]:
            category = request.GET.get("image")
            searched_images = Image.category_search(category)
            message = f"{category}"

            return render(request, 'allphotos/search.html',{"message":message,"images": searched_images})

        else:
            message = "You haven't searched for any term"
            return render(request, 'all-news/search.html',{"message":message})

def image(request,image_id):
        try:
            image = Image.objects.get(id = image_id)
        except ObjectDoesNotExist:
            raise Http404()
        return render(request,"allphotos/photo.html", {"image":image})