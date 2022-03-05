from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeContent, name='contenthome'),
    path('', views.homeContent, name='all'),
    path('article/<int:id>/', views.article, name='article'),
    path('about/', views.about, name='about'),
    path('tech/', views.tech, name='tech'),
    path('politics/', views.politics, name='politics'),
    path('sport/', views.sport, name='sports'),
    path('economics/', views.economics, name='economics'),
    path('international/', views.international, name='international'),

]
