from django.shortcuts import render

# Create your views here.
def grid(request):
    return render(request, 'grid.html')