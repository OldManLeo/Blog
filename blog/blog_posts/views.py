from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post
from .form import CommentsForm
from rest_framework import generics
from . import serializers
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import PostSerializer
from rest_framework.response import Response

class PostView(View):
    """вывод записей"""

    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog_posts/blog.html', {'post_list': posts})


class PostDetail(View):
    """Веб страница для записей"""

    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'blog_posts/blog_detail.html', {'post': post})


class AddComments(View):
    """Добавление коментариев"""

    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class UserList(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


@api_view(['POST'])
def create_post(request):
    if not request.user.is_authenticated:
        return Response({'error': 'User must be authenticated to create a post.'},
                        status=status.HTTP_401_UNAUTHORIZED)
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
