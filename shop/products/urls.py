from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_for_products, name='index'),
    path('pepa', views.new_view, name='pepa'),
]