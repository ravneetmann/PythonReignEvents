from django.urls import path
from . import views

urlpatterns =  [
    path('', views.list_event, name='list_event'),
    path('new', views.create_event, name='create_event'),
    path('update/<int:id>/', views.update_event, name='update_event'),
    path('delete/<int:id>/', views.delete_event, name='delete_event'),
]


#CRUD - CREATE, READ, UPDATE, DELETE