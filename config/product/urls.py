
from django.urls import path

from .import views
urlpatterns = [
  
    path('',views.product,name='product'),
    path('<int:pk>/',views.details,
    name='details'),
    path('<int:pk>/review/',views.review,name='review'),
    path('<int:pk>/certificate',views.certificate)
]