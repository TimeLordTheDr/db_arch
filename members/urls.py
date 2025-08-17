from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('my_first_html/', views.my_first_html, name='my_first_html'),
    path('all/', views.all, name='all'),
    path('all/details/<int:id>', views.details, name='details'),
    path('all/delete/<int:id>/', views.delete_member, name='delete_member'),
    path('all/edit/<int:id>/', views.edit_member, name='edit_member'),
    path('all/update/<int:id>/', views.update_member, name='update_member'),
    path('all/create/', views.create_member, name='create_member'),
    
    path('testing', views.testing, name='testing'),
    # path('testing/<int:id>', views.testing, name='testing'),
]