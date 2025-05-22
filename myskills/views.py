from django.shortcuts import render

# Create your views here.

def myskills(request):
    return render(request, 'skills.html')