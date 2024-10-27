from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('my_first_html/', views.my_first_html, name='my_first_html'),
    path('all/', views.all, name='all'),
    path('all/details/<int:id>', views.details, name='details'),
    # path('all/delete/<int:id>', views.delete, name='delete'),
    # path('all/edit/<int:id>', views.edit, name='edit'),
    # path('all/update/<int:id>', views.update, name='update'),
    # path('all/create', views.create, name='create'),
    # path('all/search', views.search, name='search'),
    
    path('testing', views.testing, name='testing'),
    # path('testing/<int:id>', views.testing, name='testing'),
]