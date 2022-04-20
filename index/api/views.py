from rest_framework.generics import ListCreateAPIView
from index.models import Message
from . serializers import MessageSerializer


class MessageView(ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    