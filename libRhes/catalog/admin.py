from django.contrib import admin
from django.db import models
from catalog.models import Author, Genre, Book, BookInstance, Languages

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)
admin.site.register(Languages)

