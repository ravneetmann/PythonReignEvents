from django.urls import path
from .views import list_event, create_event, update_event, delete_event

urlpatterns =  [
    path('', list_event, name='list_event'),
    path('new', create_event, name='create_event'),
    path('update/<int:id>/', update_event, name='update_event'),
    path('delete/<int:id>/', delete_event, name='delete_event'),
]


#CRUD - CREATE, READ, UPDATE, DELETE