from django.shortcuts import render

# Create your views here.
def Calendrier(request):
    return render(request, 'Calendrier.html')