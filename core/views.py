from django.shortcuts import render

# Create your views here.
def index(request):
    name = 'Husnain'
    context = {
        'name': name
    }
    return render(request, 'core/index.html', context)