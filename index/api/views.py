from rest_framework.generics import ListCreateAPIView, CreateAPIView
from index.models import Message
from . serializers import MessageSerializer


class MessageView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    