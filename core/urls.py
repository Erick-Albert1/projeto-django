from rest_framework import routers
from core import viewsets



router = routers.DefaultRouter()
router.register('customer', viewsets.CustomerViewSet)
router.register('PaymentMethod', viewsets.PaymentMethodViewSet)
router.register('Genre', viewsets.GenreViewSet)
router.register('Movie', viewsets.MovieViewSet)
router.register('MovieGenre', viewsets.MovieGenreViewSet)
router.register('Room', viewsets.RoomViewSet)
router.register('Session', viewsets.SessionViewSet)
router.register('Purchase', viewsets.PurchaseViewSet)
router.register('Ticket', viewsets.TicketViewSet)
router.register('SeatMap', viewsets.SeatMapViewSet)
router.register('RoomMap', viewsets.RoomMapViewSet)


urlpatterns = router.urls



