from django.shortcuts import render

# Create your views here.
def Classes(request):
    return render(request, 'Classes.html')