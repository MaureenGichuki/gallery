from django.http  import HttpResponse,Http404
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from .models import *

# Create your views here.
def all_images(request):
    images = Image.my_images()
    location= Location.objects.all()
    category= Location.objects.all()

    if 'location' in request.GET and request.GET['location']:
        location = request.GET.get('location')
        images = Image.location_view(location)

    elif 'category' in request.GET and request.GET['category']:
        category = request.GET.get('categories')
        images = Image.category_view(category)

    return render(request, 'allphotos/display.html', {"images":images, "location":location, "category":category})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'allphotos/display.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'allphotos/display.html',{"message":message})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"allphotos/photo.html", {"image":image})
   

