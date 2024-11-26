from django.shortcuts import render

# Create your views here.



def draww(request):
    return render(request, 'draw.html',{})