from django.urls import path

from . import views

app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'),
    # path('/', views.index, name='index'),
    path('about', views.about, name='about'),
    # path('about/', views.about, name='about'),
    path('add', views.add, name='add'),
    # path('add/', views.add, name='add'),
    path('<int:id>', views.task, name='task'),
    # path('<int:id>/', views.task, name='task'),
    path('<int:id>/update', views.update, name='update'),
    # path('<int:id>/update/', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),

]
