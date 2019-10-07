from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<int:users_id>/edit', views.edit, name='edit'),
    path('<int:users_id>/update', views.update, name='update'),
    path('store', views.store, name='store'),
    path('<int:users_id>/delete/', views.delete, name='delete'),
]
