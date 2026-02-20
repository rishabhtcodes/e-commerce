from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Category, Product
from .forms import ProductForm


@login_required
def product_create(request):
    if request.user.role != 'seller':
        messages.error(request, "Only sellers can add products.")
        return redirect('product_list')

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, f"Product '{product.name}' added successfully!")
            return redirect(product.get_absolute_url())
    else:
        form = ProductForm()

    return render(request, 'products/create.html', {'form': form})


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
