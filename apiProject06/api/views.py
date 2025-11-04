from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# Normal Query- Without Optimization
@api_view(['GET'])
def all_books(request):
    books = Book.objects.all() #N+1 Query Problem
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

# Using select_related to optimize ForeignKey relationships
@api_view(['GET'])
def select_book(request):
    books = Book.objects.select_related('author').all() #Optimized Query
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

# Using prefetch_related to optimize reverse ForeignKey relationships
@api_view(['GET'])
def prefetch_authors(request):
    authors = Author.objects.prefetch_related('books').all() #Optimized Query
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data)
