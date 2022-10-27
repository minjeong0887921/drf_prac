"""
viewset으로 api 만들기
"""
# from django.contrib.auth.models import User
# from rest_framework import viewsets

# from api2.serializers import CommentSerializer, UserSerializer, PostSerializer
# from blog.models import Comment, Post

# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer


"""
Generic Views로 api 만들기
"""
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from api2.serializers import CommentSerializer, PostListSerializer, PostRetrieveSerializer

from blog.models import Comment, Post


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostRetrieveAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostRetrieveSerializer


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer