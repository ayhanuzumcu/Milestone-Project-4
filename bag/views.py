from django.shortcuts import render, redirect

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

