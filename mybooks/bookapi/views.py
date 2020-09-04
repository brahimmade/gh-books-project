# import viewsets 
from rest_framework import viewsets 

from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from bookapi.permissions import IsOwnerOrReadOnly


# import local data 
from .serializers import BooksSerializer, UserSerializer
from .models import BooksModel 

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

# create a viewset 
class BooksViewSet(viewsets.ModelViewSet): 
	permission_classes = [permissions.IsAuthenticatedOrReadOnly,
	IsOwnerOrReadOnly]
	# define queryset 
	queryset = BooksModel.objects.order_by('id') 

	# specify serializer to be used 
	serializer_class = BooksSerializer 

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

	def perform_update(self, serializer):
		serializer.save(owner=self.request.user)
