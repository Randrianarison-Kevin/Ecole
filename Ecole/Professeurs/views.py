from django.shortcuts import render
from .models import Prof
# Create your views here.
def Prof_list(request):  
    Profs = Prof.objects.all()
    return render(request, 'Prof.html', context={'Profs':Profs} )