# Filtros de pesquisa
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
from .models import Customer, Movie, Session, Purchase, Room, Ticket

class CustomerFilter(django_filters.FilterSet):
    email = django_filters.CharFilter(lookup_expr='icontains')
    name = django_filters.CharFilter(lookup_expr='icontains')
    date_birth = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Customer
        fields = ['email', 'name', 'date_birth', 'active']

class MovieFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    parental_rating = django_filters.NumberFilter(lookup_expr='exact')

    class Meta:
        model = Movie
        fields = ['name', 'parental_rating', 'active']

class SessionFilter(django_filters.FilterSet):
    movie = django_filters.CharFilter(field_name='movie__name', lookup_expr='icontains')
    room_number = django_filters.CharFilter(field_name='room__room_number', lookup_expr='exact')
    date_time = django_filters.DateTimeFromToRangeFilter()

    class Meta:
        model = Session
        fields = ['date_time', 'movie', 'room']

class PurchaseFilter(django_filters.FilterSet):
    customer_name = django_filters.CharFilter(field_name='customer__name', lookup_expr='icontains')
    payment_method = django_filters.CharFilter(field_name='payment_method__name', lookup_expr='icontains')
    date_time = django_filters.DateTimeFromToRangeFilter()

    class Meta:
        model = Purchase
        fields = ['customer', 'payment_method', 'date_time']

class TicketFilter(django_filters.FilterSet):
    purchase_id = django_filters.NumberFilter(field_name='purchase__id', lookup_expr='exact')
    session_id = django_filters.NumberFilter(field_name='session__id', lookup_expr='exact')
    seat_position = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Ticket
        fields = ['purchase', 'session', 'seat_position']

class RoomFilter(django_filters.FilterSet):
    room_number = django_filters.CharFilter(lookup_expr='icontains')
    room_type = django_filters.NumberFilter(lookup_expr='exact')

    class Meta:
        model = Room
        fields = ['room_number', 'room_type']