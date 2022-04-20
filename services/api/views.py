from rest_framework.generics import ListAPIView
from services.models import Services
from . serializers import ServicesSerializer


class ServicesView(ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    