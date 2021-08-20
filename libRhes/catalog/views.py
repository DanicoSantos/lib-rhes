from django.shortcuts import render

from rest_framework import viewsets

from .models import Author, Book, BookInstance
from .serializers import AuthorSerializer, BookSerializer, BookInstanceSerializer


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookInstanceViewSet(viewsets.ModelViewSet):
    serializer_class = BookInstanceSerializer
    queryset = BookInstance.objects.all()

    def get_queryset(self):
        return self.queryset.filter(status="m")


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
