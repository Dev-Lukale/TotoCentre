from django.urls import path
from . import views as Posts_views
from .views import (
	PostListView,
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView)
urlpatterns = [
 path('posts/', PostListView.as_view(),name='Posts_view'),
 path('posts/<int:pk>/', PostDetailView.as_view(),name='Posts_detail'),
 path('posts/new/', PostCreateView.as_view(),name='Posts_create'),
 path('posts/<int:pk>/update', PostUpdateView.as_view(),name='Posts_update'),
 path('posts/<int:pk>/delete', PostDeleteView.as_view(),name='Posts_delete'),
 
 ]
