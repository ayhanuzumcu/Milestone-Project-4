from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
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
                messages.success(request, f'Updated {product.name} with {drink.upper()} quantity to {bag[item_id]["items_by_drink"][drink]}')
            else:
                bag[item_id]['items_by_drink'][drink] = quantity
                messages.success(request, f'Added {product.name} with {drink.upper()} to your basket')
        else:
            bag[item_id] = {'items_by_drink': {drink: quantity}}
            messages.success(request, f'Added {product.name} with {drink.upper()} to your basket')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your basket')

    request.session['bag'] = bag
    return redirect(redirect_url)
    

def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    drink = None
    if 'free_drink' in request.POST:
        drink = request.POST['free_drink']
    bag = request.session.get('bag', {})

    if drink:
        if quantity > 0:
            bag[item_id]['items_by_drink'][drink] = quantity
            messages.success(request, f'Updated {product.name} with {drink.upper()} quantity to {bag[item_id]["items_by_drink"][drink]}')
        else:
            del bag[item_id]['items_by_drink'][drink]
            if not bag[item_id]['items_by_drink']:
                bag.pop(item_id)
            messages.success(request, f'Removed {product.name} with {drink.upper()} from your basket')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your basket')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        drink = None
        if 'free_drink' in request.POST:
            drink = request.POST['free_drink']
        bag = request.session.get('bag', {})

        if drink:
            del bag[item_id]['items_by_drink'][drink]
            if not bag[item_id]['items_by_drink']:
                bag.pop(item_id)
            messages.success(request, f'Removed {product.name} with {drink.upper()} from your basket')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your basket')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)