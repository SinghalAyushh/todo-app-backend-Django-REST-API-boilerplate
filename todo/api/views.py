from rest_framework import viewsets
from todo.models import Postt
from .serializers import PostSerializer
  
class TodoView(viewsets.ModelViewSet):      
      serializer_class = PostSerializer         
      queryset = Postt.objects.all()  
