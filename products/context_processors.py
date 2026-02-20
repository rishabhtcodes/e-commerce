from .models import Category

def category_processor(request):
    """
    Makes all root categories available in every template
    so the navbar can render a dropdown menu globally.
    """
    categories = Category.objects.filter(parent=None)
    return {'global_categories': categories}
