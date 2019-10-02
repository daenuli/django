from django.urls import path

from . import views

app_name = 'article'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<int:article_id>/edit', views.edit, name='edit'),
    path('<int:article_id>/update', views.update, name='update'),
    path('store', views.store, name='store'),
    path('<int:article_id>/delete/', views.delete, name='delete'),
]
