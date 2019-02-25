from rest_framework.serializers import ModelSerializer
from .models import Authors,Books


class BooksSerializer(ModelSerializer): # BooksSerializer must be above AuthorsSerializer
    class Meta:
        model=Books
        fields='__all__'


class AuthorsSerializer(ModelSerializer):
    books_by_author=BooksSerializer(read_only=True,many=True)
    class Meta:
        model=Authors
        fields='__all__'
