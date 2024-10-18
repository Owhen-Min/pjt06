from django.urls import path
from . import views

app_name = 'boards'
urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('create/', views.create, name = 'create'),
    path('<int:pk>', views.detail, name = 'detail'),
]