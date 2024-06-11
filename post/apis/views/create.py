from rest_framework.views import APIView
from rest_framework import status, permissions
from ..serializers import PostSerializer, Post
from rest_framework.response import Response

class create_post_view(APIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def post (self, request, **kwrags) : 
        serializer = self.serializer_class(data=request.data, context={'user':request.user})
        if serializer.is_valid() : 
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        