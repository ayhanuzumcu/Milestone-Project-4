from django.shortcuts import render

# Create your views here.


def info(request):
    """ A view to return the index page """

    return render(request, 'info/info.html')
