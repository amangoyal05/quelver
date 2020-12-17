from django.urls import path
from . import views
from .views import QueriesView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, LikeView

urlpatterns = [
    path('', views.home, name="home"),
    path('Queries/', QueriesView.as_view(), name="queries"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail" ),
    path('add_post/',  AddPostView.as_view(), name='add_query'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_query'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_query'),
    path('like/<int:pk>', LikeView, name='like_post'),
]