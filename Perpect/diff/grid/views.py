from django.shortcuts import render

# Create your views here.
def grid(request):
    for_index = range(8)
    return render(request, 'grid.html',{'for_index':for_index})