from rest_framework import viewsets
from core import models, serializers
from rest_framework.permissions import IsAuthenticated
from . import filters
import django_filters


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
    filterset_class = filters.CustomerFilter
    permission_classes = [IsAuthenticated]


class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = models.PaymentMethod.objects.all()
    serializer_class = serializers.PaymentMethodSerializer
    filterset_class = filters.PaymentMethodFilter
    permission_classes = [IsAuthenticated]



class GenreViewSet(viewsets.ModelViewSet):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer
    filterset_class = filters.GenreFilter
    permission_classes = [IsAuthenticated]



class MovieViewSet(viewsets.ModelViewSet):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer
    filterset_class = filters.MovieFilter
    permission_classes = [IsAuthenticated]


class MovieGenreViewSet(viewsets.ModelViewSet):
    queryset = models.MovieGenre.objects.all()
    serializer_class = serializers.MovieGenreSerializer
    filterset_class = filters.MovieGenreFilter
    permission_classes = [IsAuthenticated]



class RoomViewSet(viewsets.ModelViewSet):
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer
    filterset_class = filters.RoomFilter
    permission_classes = [IsAuthenticated]


class RoomMapViewSet(viewsets.ModelViewSet):
    queryset = models.RoomMap.objects.all()
    serializer_class = serializers.RoomMapSerializer
    filterset_class = filters.RoomMapFilter
    permission_classes = [IsAuthenticated]



class SessionViewSet(viewsets.ModelViewSet):
    queryset = models.Session.objects.all()
    serializer_class = serializers.SessionSerializer
    filterset_class = filters.SessionFilter
    permission_classes = [IsAuthenticated]


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = models.Purchase.objects.all()
    serializer_class = serializers.PurchaseSerializer
    filterset_class = filters.PurchaseFilter
    permission_classes = [IsAuthenticated]


class TicketViewSet(viewsets.ModelViewSet):
    queryset = models.Ticket.objects.all()
    serializer_class = serializers.TicketSerializer
    filterset_class = filters.TicketFilter
    permission_classes = [IsAuthenticated]


class SeatMapViewSet(viewsets.ModelViewSet):
    queryset = models.SeatMap.objects.all()
    serializer_class = serializers.SeatMapSerializer
    filterset_class = filters.SeatMapFilter
    permission_classes = [IsAuthenticated]