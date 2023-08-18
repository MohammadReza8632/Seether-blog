from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .cart import Cart
from seetherstore.models import Product, Category, SubCategory


def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return render(request, 'menu_cart.html')


def cart(request):
    categories = Category.objects.all()
    sub_category = SubCategory.objects.all()

    context = {

        'categories': categories,
        'sub_category': sub_category,


    }
    return render(request, 'cart.html', context)


def update_cart(request, product_id, action):
    cart = Cart(request)

    if action == 'increment':
        cart.add(product_id, 1, True)
    else:
        cart.add(product_id, -1, True)

    product = Product.objects.get(pk=product_id)
    quantity = cart.get_item(product_id)

    if quantity:
        quantity = quantity['quantity']

        item = {
            'product': {
                'id': product.id,
                'name': product.name,
                'image': product.image,
                'price': product.price,
            },
            'total_price': (quantity * product.price),
            'quantity': quantity,
        }
    else:
        item = None
    response = render(request, 'cart_item.html', {'item': item})
    response['HX-Trigger'] = 'update-menu-cart'

    return response


@login_required
def checkout(request):
    categories = Category.objects.all()
    sub_category = SubCategory.objects.all()

    context = {

        'categories': categories,
        'sub_category': sub_category,

    }
    return render(request, 'checkout.html', context)


def hx_menu_cart(request):
    return render(request, 'menu_cart.html')


def hx_cart_total(request):
    return render(request, 'cart_total.html')
