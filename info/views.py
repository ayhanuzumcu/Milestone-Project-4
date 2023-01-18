from django.shortcuts import render

# Create your views here.


def info(request):
    """ A view to return the info page """

    return render(request, 'info/info.html')


def delivery_info(request):
    """ A view to return the delivery information page """

    return render(request, 'info/delivery_info.html')


def contact_info(request):
    """ A view to return the delivery information page """

    return render(request, 'info/contact_info.html')
