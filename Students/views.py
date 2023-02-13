from django.shortcuts import render

# Create your views here.

def Student_Home(request):
    return render(request, 'Page1.html')