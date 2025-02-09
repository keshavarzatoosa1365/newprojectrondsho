from django.urls import path
from .views import BlogPostListView, BlogPostDetailView, BlogPostUpdateView, BlogPostSearchView

app_name = 'api'

urlpatterns = [
    path('blog-posts/', BlogPostListView.as_view(), name='blog-post-list'),
    path('blog-post/<int:pk>', BlogPostDetailView.as_view(), name='blog-post-detail'),
    path('blog-post-update/<int:pk>', BlogPostUpdateView.as_view(), name='blog-post-update'),
    path('blog-posts-search/', BlogPostSearchView.as_view(), name='blog-post-search'),
]