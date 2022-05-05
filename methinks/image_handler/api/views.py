from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from ..models import Image, Comment
from .serializers import ImageSerializer, CommentSerializer

class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer

class CommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        # pk = self.request.query_params.get('image_id', None)
        # if pk is None:
        #     return Comment.objects.all()
        # else:
        #     img = get_object_or_404(Image, pk=pk)
        #     return img.comments.filter(active=True)
        img = get_object_or_404(Image, pk=self.kwargs['pk'])
        return img.comments.filter(active=True)

class ImageListView(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageDetailView(generics.RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageUploadView(APIView):
    # autentication_classes = (BasicAuthentication,)
    # permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser,)

    def get(self, request):
        return Response({'good': True}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        print(request.data)
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)