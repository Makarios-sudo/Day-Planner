from django.urls import path
from .import views




urlpatterns = [ 
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('plans/', views.plans, name='plans'),
    path('plan/<str:pk>/', views.plan, name='plan'),
    path('addplan/', views.addplan, name='addplan' ),
    path('update/<str:pk>/', views.update, name='update'),
    path('delete/<str:pk>', views.delete, name='delete') ,

]