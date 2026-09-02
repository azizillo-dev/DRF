from .serializers import *
from rest_framework.response import Response
from .models import Post
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from users.permissions import *


class CreatePostView(APIView):
    permission_classes = [IsLoggedIn]

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)

        return Response({
            "msg": "Post created!",
            "post": serializer.data
        }, status=status.HTTP_201_CREATED)


class PostListView(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response({
            "msg": "All posts",
            "posts": serializer.data
        }, status=status.HTTP_200_OK)


class PostUpdateView(APIView):
    permission_classes = [IsLoggedIn, IsOwner]
    def patch(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        self.check_object_permissions(request, post)
        serializer = PostSerializer(
            instance=post,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "msg": "Post updated",
            "data": serializer.data
        })


class PostDeleteView(APIView):
    permission_classes = [IsLoggedIn, IsOwner]

    def delete(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        self.check_object_permissions(request, post)
        post.delete()
        return Response({
            "msg": "Post deleted!"
        }, status=status.HTTP_204_NO_CONTENT)