LIKE = 'unaccent__icontains' # Usando unaccent para ignorar acentos e trazer palavras semelhantes
ICONTAINS = 'icontains' # Usando icontains para trazer palavras semelhantes
UNACCENT_IEXACT = 'unaccent__iexact' # Usando unaccent para ignorar acentos e trazer palavras exatas
EQUALS = 'exact' # Usando exact para trazer o campo exatas
STARTS_WITH = 'startswith' # Usando startswith para trazer palavras que começam com o termo pesquisado
GT = 'gt' # maior que
LT = 'lt' # menor que
GTE = 'gte' # maior ou igual a
LTE = 'lte' # menor ou igual a
IN = 'in' # Usando in para trazer palavras que estão na lista

import django_filters
from .models import (
    Customer,
    PaymentMethod,
    Genre,
    Movie,
    MovieGenre,
    Room,
    RoomMap,
    Session,
    Purchase,
    Ticket,
    SeatMap
)


class CustomerFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    date_birth = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'date_birth', 'active']


class PaymentMethodFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = PaymentMethod
        fields = ['id', 'name', 'active']


class GenreFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Genre
        fields = ['id', 'name', 'active']


class MovieFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    parental_rating = django_filters.NumberFilter(lookup_expr='exact')

    class Meta:
        model = Movie
        fields = ['id', 'name', 'parental_rating', 'active']


class MovieGenreFilter(django_filters.FilterSet):
    movie = django_filters.NumberFilter(lookup_expr='exact')
    genre = django_filters.NumberFilter(lookup_expr='exact')
    movie_name = django_filters.CharFilter(field_name='movie__name', lookup_expr='icontains')
    genre_name = django_filters.CharFilter(field_name='genre__name', lookup_expr='icontains')

    class Meta:
        model = MovieGenre
        fields = ['id', 'movie', 'genre']


class RoomFilter(django_filters.FilterSet):
    room_number = django_filters.CharFilter(lookup_expr='icontains')
    room_type = django_filters.NumberFilter(lookup_expr='exact')
    seat_capacity = django_filters.NumberFilter(lookup_expr='gte') # Maior ou igual a

    class Meta:
        model = Room
        fields = ['id', 'room_number', 'room_type', 'seat_capacity', 'active']


class RoomMapFilter(django_filters.FilterSet):
    room = django_filters.NumberFilter(lookup_expr='exact')
    room_number = django_filters.CharFilter(field_name='room__room_number', lookup_expr='icontains')

    class Meta:
        model = RoomMap
        fields = ['id', 'room', 'active']


class SessionFilter(django_filters.FilterSet):
    movie = django_filters.NumberFilter(lookup_expr='exact')
    room = django_filters.NumberFilter(lookup_expr='exact')
    date_time = django_filters.DateTimeFromToRangeFilter()
    movie_name = django_filters.CharFilter(field_name='movie__name', lookup_expr='icontains')
    room_number = django_filters.CharFilter(field_name='room__room_number', lookup_expr='exact')

    class Meta:
        model = Session
        fields = ['id', 'movie', 'room', 'date_time', 'active']


class PurchaseFilter(django_filters.FilterSet):
    customer = django_filters.NumberFilter(lookup_expr='exact')
    payment_method = django_filters.NumberFilter(lookup_expr='exact')
    date_time = django_filters.DateTimeFromToRangeFilter()
    customer_name = django_filters.CharFilter(field_name='customer__name', lookup_expr='icontains')
    payment_method_name = django_filters.CharFilter(field_name='payment_method__name', lookup_expr='icontains')

    class Meta:
        model = Purchase
        fields = ['id', 'customer', 'payment_method', 'date_time', 'active']


class TicketFilter(django_filters.FilterSet):
    purchase = django_filters.NumberFilter(lookup_expr='exact')
    session = django_filters.NumberFilter(lookup_expr='exact')
    seat_position = django_filters.CharFilter(lookup_expr='icontains')
    purchase_customer_name = django_filters.CharFilter(field_name='purchase__customer__name', lookup_expr='icontains')

    class Meta:
        model = Ticket
        fields = ['id', 'purchase', 'session', 'seat_position', 'active']


class SeatMapFilter(django_filters.FilterSet):
    session = django_filters.NumberFilter(lookup_expr='exact')
    movie_name = django_filters.CharFilter(field_name='session__movie__name', lookup_expr='icontains')
    room_number = django_filters.CharFilter(field_name='session__room__room_number', lookup_expr='icontains')

    class Meta:
        model = SeatMap
        fields = ['id', 'session', 'active']