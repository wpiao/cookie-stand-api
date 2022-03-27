from .models import CookieStand
from .serializer import CookieStandSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class CookieStandList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = CookieStand.objects.all()
    serializer_class = CookieStandSerializer

class CookieStandDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = CookieStand.objects.all()
    serializer_class = CookieStandSerializer

