from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import AuthorViewSet, BookViewSet, BookInstanceViewSet

router = DefaultRouter()
router.register('books', BookViewSet, basename='books')
router.register('book-instances', BookInstanceViewSet, basename='book_instances')
router.register('author', AuthorViewSet, basename='author')

urlpatterns = [
    path('', include(router.urls)),
]
