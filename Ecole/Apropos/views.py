from django.shortcuts import render

# Create your views here.
def Apropos(request):
    return render(request, 'Apropos.html')