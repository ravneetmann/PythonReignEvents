from django.urls import path
from .views import list_product, create_product, update_product, delete_product

urlpatterns =  [
    path('', list_product, name='list_product'),
    path('new', create_product, name='create_product'),
    path('update/<int:id>/', update_product, name='update_product'),
    path('delete/<int:id>/', delete_product, name='delete_product'),
]


#CRUD - CREATE, READ, UPDATE, DELETE