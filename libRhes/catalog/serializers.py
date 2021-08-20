from django.db.models import fields
from rest_framework import serializers

from .models import Author, Book, BookInstance



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'author',
            'summary',
            'isbn',
            'display_genre',
        )
        depth = 2

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
        depth = 3

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'id',
            'first_name',
            'last_name',
            '__str__'
        )