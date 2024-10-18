from django.urls import path
from . import views

app_name = 'boards'
urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('create/', views.create, name = 'create'),
    path('<int:board_pk>/',views.create_comment, name='create_comment'),
]