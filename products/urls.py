from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views
from .views import HelloAPI, booksAPI, bookAPI, BookAPI, BooksAPI


router = DefaultRouter()
router.register('product', views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("hello/", HelloAPI),
    path("fbv/books/", booksAPI),
    path("fbv/book/<int:bid>", bookAPI),
    path("cbv/books/", BooksAPI.as_view()),
    path("cbv/book/<int:bid>", BookAPI.as_view()),

]