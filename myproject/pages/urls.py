#from django.urls import path
#from . import views

#urlpatterns = [
#    path('data/', views.data_page, name='data'),
#    path('test/', views.test_page, name='test'),
#]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),  # главная страница
    path('data/', views.data_page, name='data'),
    path('test/', views.test_page, name='test'),
]