from rest_framework import serializers
from products.models import Product
from .models import Book

class ProductSerializer(serializers.ModelSerializer):
    class Meta:

        model = Product
        fields = (
            'id',
            'product_name',
            'price'
        )

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['bid', 'title', 'author', 'category', 'pages', 'price', 'published_date', 'description']