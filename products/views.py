from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import ProductSerializer
from .models import Product
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from .serializer import BookSerializer



class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
# Create your views here.

# @api_view(['GET'])
# def HelloAPI(request):
#     return Response('Hello World!')


# @api_view(['GET', 'POST'])
# def booksAPI(request):
#     if request.method == 'GET':
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True) # 시리얼라이저에 전체 데이터 한 번에 집어넣기
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = BookSerializer(data=request.data) # 시리얼라이저에 POST 요청으로 들어온 데이터 넣기
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def bookAPI(request, bid):
#     book = get_object_or_404(Book, bid=bid) # Book에서 bid = id인 데이터 가져오고 없으면 404에러, 딱 book 객체 하나만 가져옴
#     serializer = BookSerializer(book)
#     return Response(serializer.data, status=status.HTTP_200_OK)
#
#함수형 뷰
##############################

class HelloAPI(APIView):
    def get(self, request):
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookAPI(APIView):
    def get(self, request, bid):
        book = get_object_or_404(Book, bid=bid)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
#클래스 기반 뷰