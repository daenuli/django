from django.urls import path

from . import views

app_name = 'category'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<int:category_id>/edit', views.edit, name='edit'),
    path('<int:category_id>/update', views.update, name='update'),
    path('store', views.store, name='store'),
    path('<int:category_id>/delete/', views.delete, name='delete'),
]
