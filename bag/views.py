from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.


def view_bag(request):
    """ A view that renders the bag content page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    drink = None
    if 'free_drink' in request.POST:
        drink = request.POST['free_drink']
    bag = request.session.get('bag', {})

    if drink:
        if item_id in list(bag.keys()):
            if drink in bag[item_id]['items_by_drink'].keys():
                bag[item_id]['items_by_drink'][drink] += quantity
            else:
                bag[item_id]['items_by_drink'][drink] = quantity
        else:
            bag[item_id] = {'items_by_drink': {drink: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    drink = None
    if 'free_drink' in request.POST:
        drink = request.POST['free_drink']
    bag = request.session.get('bag', {})

    if drink:
        if quantity > 0:
            bag[item_id]['items_by_drink'][drink] = quantity
        else:
            del bag[item_id]['items_by_drink'][drink]
            if not bag[item_id]['items_by_drink']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        drink = None
        if 'free_drink' in request.POST:
            drink = request.POST['free_drink']
        bag = request.session.get('bag', {})

        if drink:
            del bag[item_id]['items_by_drink'][drink]
            if not bag[item_id]['items_by_drink']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
