from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import ListView
from .models import Category, Product, SubCategory
from django.db.models import Q
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required


def store_home(request):
    categories = Category.objects.all()
    sub_category = SubCategory.objects.all()
    products = Product.objects.all()[0:12]

    context = {

        'categories': categories,
        'sub_category': sub_category,
        'products': products,

    }

    return render(request, 'store_home.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('/seetherstore')
    else:
        form = SignUpForm()
    categories = Category.objects.all()
    sub_category = SubCategory.objects.all()

    context = {

        'categories': categories,
        'sub_category': sub_category,
        'form': form

    }
    return render(request, 'signup.html', context)


@login_required
def myaccount(request):
    categories = Category.objects.all()
    sub_category = SubCategory.objects.all()

    context = {

        'categories': categories,
        'sub_category': sub_category,

    }
    return render(request, 'myaccount.html', context)


@login_required
def edit_myaccount(request):
    categories = Category.objects.all()
    sub_category = SubCategory.objects.all()

    context = {

        'categories': categories,
        'sub_category': sub_category,

    }
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()

        return redirect('myaccount')

    return render(request, 'edit_myaccount.html', context)


def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    sub_category = SubCategory.objects.all()

    active_category = request.GET.get('category', '')

    if active_category:
        products = products.filter(Q(category__slug=active_category) | Q(sub_category__slug=active_category))

    query = request.GET.get('query', '')
    if query:
        products = products.filter(name__icontains=query)

    context = {

        'categories': categories,
        'sub_category': sub_category,
        'active_category': active_category,
        'products': products,

    }

    return render(request, 'shop.html', context)


def product_detail(request, slug):
    products = Product.objects.get(slug=slug)
    categories = Category.objects.all()
    sub_category = SubCategory.objects.all()

    context = {

        'categories': categories,
        'sub_category': sub_category,
        'products': products,

    }
    return render(request, 'store_detail.html', context)


"""class VinylListView(ListView):
    model = Product
    template_name = "VINYL.html"
    ordering = ["-created"]


class AccessoriesListView(ListView):
    model = Product
    template_name = "Accessories.html"
    ordering = ["-created"]"""
