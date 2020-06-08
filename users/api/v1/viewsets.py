from rest_framework import authentication
from users.models import Fddgfghf
from .serializers import FddgfghfSerializer
from rest_framework import viewsets


class FddgfghfViewSet(viewsets.ModelViewSet):
    serializer_class = FddgfghfSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Fddgfghf.objects.all()
