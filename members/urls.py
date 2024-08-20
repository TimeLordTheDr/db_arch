from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('all/', views.all, name='all'),
    path('all/details/<int:id>', views.details, name='details'),
]