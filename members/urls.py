from django.urls import path
from . import views

urlpatterns = [
    path('my_first_html/', views.my_first_html, name='my_first_html'),
    path('all/', views.all, name='all'),
    path('all/details/<int:id>', views.details, name='details'),
]