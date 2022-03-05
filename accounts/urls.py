from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginadmin, name='login'),
    path('login/', views.loginadmin, name='login'),
    path('logout/', views.logoutadmin, name ='logout'),
    path('index/', views.dashboard, name='adminindex'),
    path('register/', views.register, name='admin-register'),
    path('createpost/', views.createPost, name='createpost'),
    path('viewpost/', views.viewPost, name='viewpost'),

]
