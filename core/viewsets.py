from rest_framework import viewsets
from core import models, serializers
from rest_framework.permissions import IsAuthenticated
import filters


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
    filterset_class = filters.CustomerFilter
    permission_classes = [IsAuthenticated]


class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = models.PaymentMethodViewSet.objects.all()
    serializer_class = serializers.PaymentMethodViewSetSerializer
    filterset_class = filters.PaymentMethodViewSetFilter
    permission_classes = [IsAuthenticated]



class GenreViewSet(viewsets.ModelViewSet):
    queryset = models.GenreViewSet.objects.all()
    serializer_class = serializers.GenreViewSetSerializer
    filterset_class = filters.GenreViewSetFilter
    permission_classes = [IsAuthenticated]



class MovieViewSet(viewsets.ModelViewSet):
    queryset = models.MovieViewSet.objects.all()
    serializer_class = serializers.MovieViewSetSerializer
    filterset_class = filters.MovieViewSetFilter
    permission_classes = [IsAuthenticated]


class MovieGenreViewSet(viewsets.ModelViewSet):
    queryset = models.MovieGenreViewSet.objects.all()
    serializer_class = serializers.MovieGenreViewSetSerializer
    filterset_class = filters.MovieGenreViewSetFilter
    permission_classes = [IsAuthenticated]



class RoomViewSet(viewsets.ModelViewSet):
    queryset = models.RoomViewSet.objects.all()
    serializer_class = serializers.RoomViewSetSerializer
    filterset_class = filters.RoomViewSetFilter
    permission_classes = [IsAuthenticated]


class RoomMapViewSet(viewsets.ModelViewSet):
    queryset = models.RoomMapViewSet.objects.all()
    serializer_class = serializers.RoomMapViewSetSerializer
    filterset_class = filters.RoomMapViewSetFilter
    permission_classes = [IsAuthenticated]



class SessionViewSet(viewsets.ModelViewSet):
    queryset = models.SessionViewSet.objects.all()
    serializer_class = serializers.SessionViewSetSerializer
    filterset_class = filters.SessionViewSetFilter
    permission_classes = [IsAuthenticated]


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = models.PurchaseViewSet.objects.all()
    serializer_class = serializers.PurchaseViewSetSerializer
    filterset_class = filters.PurchaseViewSetFilter
    permission_classes = [IsAuthenticated]


class TicketViewSet(viewsets.ModelViewSet):
    queryset = models.TicketViewSet.objects.all()
    serializer_class = serializers.TicketViewSetSerializer
    filterset_class = filters.TicketViewSetFilter
    permission_classes = [IsAuthenticated]


class SeatMapViewSet(viewsets.ModelViewSet):
    queryset = models.SeatMapViewSet.objects.all()
    serializer_class = serializers.SeatMapViewSetSerializer
    filterset_class = filters.SeatMapViewSetFilter
    permission_classes = [IsAuthenticated]