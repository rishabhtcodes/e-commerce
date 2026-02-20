from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('create/', views.product_create, name='product_create'),
    path('action/<int:product_id>/delete/', views.product_delete, name='product_delete'),
    path('action/<int:product_id>/toggle-stock/', views.product_toggle_stock, name='product_toggle_stock'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
]
