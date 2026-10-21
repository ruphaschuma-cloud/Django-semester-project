from django.shortcuts import render


def product_list(request):
    products = ['Laptop', 'Phone', 'Headphones']
    return render(request, 'products/product_list.html', {'products': products})
