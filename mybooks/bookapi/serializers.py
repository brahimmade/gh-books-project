from django.contrib.auth.models import User

# import serializer from rest_framework 
from rest_framework import serializers 

# import model from models.py 
from .models import BooksModel

class UserSerializer(serializers.HyperlinkedModelSerializer):
    bookapi = serializers.HyperlinkedRelatedField(many=True, view_name='bookapi-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'bookapi']

class BooksSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = BooksModel
        fields = ('id', 'book_title', 'file', 'book_type', 'owner')