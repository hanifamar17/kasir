from django.urls import path
from . import views

urlpatterns = [
    path('', views.cashier_view, name='cashier'),
    path('get-product/', views.get_product, name='get_product'),
    path('save-transaction/', views.save_transaction, name='save_transaction'),
    path('search-employees/', views.search_employees, name='search_employees'),
    path('search-customers/', views.search_customers, name='search_customers'),
]