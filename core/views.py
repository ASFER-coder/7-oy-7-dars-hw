from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer
from rest_framework.views import APIView

@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        author = request.GET.get('author')
        if author:
            books = Book.objects.filter(author=author)
        else:
            books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Kitob muvaffaqiyatli qo‘shildi",
                "book": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookListAPIView(APIView):

    def get(self, request):
        author = request.GET.get('author')
        if author:
            books = Book.objects.filter(author=author)
        else:
            books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Kitob muvaffaqiyatli qoshildi",
                "book": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
