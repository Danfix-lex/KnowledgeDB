from rest_framework import serializers

from catalogue.models import Book, Author, BookImage


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'email', 'dob']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True, read_only=True)
    images = serializers.HyperlinkedRelatedField(
        view_name='book-image-detail',
        queryset=BookImage.objects.all(),
        many=True
    )

    class Meta:
        model = Book
        fields = ['id', 'title', 'summary','images', 'author']

class AddBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'isbn', 'summary']

class BookImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookImage
        fields = ['id', 'image']