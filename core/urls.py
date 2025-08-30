from rest_framework import routers

from .viewsets import (
    CustomerViewSet,
    PaymentMethodViewSet,
    GenreViewSet,
    MovieViewSet,
    MovieGenreViewSet,
    RoomViewSet,
    RoomMapViewSet,
    SessionViewSet,
    PurchaseViewSet,
    TicketViewSet,
    SeatMapViewSet
)

router = routers.DefaultRouter()
router.register('customers', CustomerViewSet, basename='customer')
router.register('payment_methods', PaymentMethodViewSet, basename='payment-method')
router.register('genres', GenreViewSet, basename='genre')
router.register('movies', MovieViewSet, basename='movie')
router.register('movie_genres', MovieGenreViewSet, basename='movie-genre')
router.register('rooms', RoomViewSet, basename='room')
router.register('room_maps', RoomMapViewSet, basename='room-map')
router.register('sessions', SessionViewSet, basename='session')
router.register('purchases', PurchaseViewSet, basename='purchase')
router.register('tickets', TicketViewSet, basename='ticket')
router.register('seat_maps', SeatMapViewSet, basename='seat-map')

urlpatterns = router.urls