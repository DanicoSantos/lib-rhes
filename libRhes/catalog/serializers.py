from django.db.models import fields
from rest_framework import serializers

from .models import Book, BookInstance


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'author',
            'summary',
            'isbn',
            'genre'
        )

7
class BookInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInstance
        fields = (
            'id',
            'book',
            'imprint',
            'due_back',
            'status',
            'language'
        )
