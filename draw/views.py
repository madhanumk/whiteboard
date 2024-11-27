from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.text import slugify
from .models import Classroom
# Create your views here.

def home(request):
    return render(request, 'home.html',{})

def draw(request,slug):
    return render(request, 'draw.html',{'slug':slug})


@csrf_exempt
def create_classroom(request):
    if request.method == "POST":
        name = request.POST.get("name")
        slug = slugify(name)

        # Create a new classroom
        classroom = Classroom.objects.create(name=name, slug=slug)

        # Return the data in JSON format
        return JsonResponse({"name": classroom.name, "slug": classroom.slug})

    return JsonResponse({"error": "Invalid request method"}, status=400)

