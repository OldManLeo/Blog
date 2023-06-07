from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import create_post


urlpatterns = [path('', views.PostView.as_view()),
               path('<int:pk>/', views.PostDetail.as_view()),
               path('review/<int:pk>', views.AddComments.as_view(), name='add_comments'),
               path('users/', views.UserList.as_view()),
               path('users/<int:pk>', views.UserDetail.as_view()),
               path('posts/', views.PostList.as_view()),
               path('posts/<int:pk>', views.PostDetailApi.as_view()),
               path('posts/', create_post, name='create_post')]

urlpatterns = format_suffix_patterns(urlpatterns)

