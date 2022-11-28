from rest_framework import viewsets
from .models import ChatResponse
from .serializers import ChatResponseSerializer


class ChatViewSet(viewsets.ModelViewSet):
    serializer_class = ChatResponseSerializer
    queryset = ChatResponse.objects.all()

