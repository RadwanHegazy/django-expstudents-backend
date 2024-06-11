from rest_framework.views import APIView
from rest_framework import status
from ..serializers import PostSerializer, Post
from rest_framework.response import Response

class get_posts_view(APIView):
    serializer_class = PostSerializer
    
    def get(self, request, **kwargs) : 
        data = Post.objects.all()
        serializer = self.serializer_class(data,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)