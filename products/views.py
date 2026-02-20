from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Category, Product


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.filter(parent=None)
    products = Product.objects.filter(is_available=True).select_related('category')

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    query = request.GET.get('q')
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))

    sort = request.GET.get('sort')
    if sort == 'price_low':
        products = products.order_by('price')
    elif sort == 'price_high':
        products = products.order_by('-price')
    else:
        products = products.order_by('-created_at')

    # Pagination — 12 products per page
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'products/list.html', {
        'category': category,
        'categories': categories,
        'products': page_obj,
        'page_obj': page_obj,
    })


def product_detail(request, category_slug, product_slug):
    product = get_object_or_404(
        Product.objects.select_related('category'),
        slug=product_slug,
        category__slug=category_slug,
        is_available=True
    )
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    return render(request, 'products/detail.html', {
        'product': product,
        'related_products': related_products
    })
