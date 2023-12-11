from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/login/', views.login, name='login'),
    path('home/register/', views.register, name='register'),
    path('home/register/insertdata/', views.insertdata, name='insertdata'),
    path('home/login/checkdata/', views.checkdata, name='checkdata'),
    path('home/table/', views.table, name='table'),
    path('home/table/delete/<int:id>', views.delete, name='delete'),
    path('home/table/update/<int:id>', views.update , name='update'),
    path('home/table/update/updatedata/<int:id>', views.updatedata , name='updatedata'),
    #path('home/login/register/', views.register, name='register'),
]