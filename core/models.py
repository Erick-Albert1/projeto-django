from django.db import models


class ModelBase(models.Model):
    id = models.BigAutoField(
        db_column='id',
        null=False,
        primary_key=True,
    )
    created_at = models.DateTimeField(
        db_column='dt_created_at',
        auto_now_add=True,
        null=False,
    )
    modified_at = models.DateTimeField(
        db_column='dt_modified_at',
        auto_now=True,
        null=False,
    )
    active = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
    )

    class Meta:
        abstract = True
        managed = True


class Customer(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        null=True,
        blank=True,
        max_length=120,
    )
    date_birth = models.DateField(
        db_column='dt_date_birth',
        null=False,
        blank=False,
    )
    email = models.EmailField(
        db_column='tx_email',
        null=False,
        blank=False,
        unique=True,
    )

    def __str__(self):
        return self.name or str(self.id)

    class Meta:
        db_table = 'customer'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


class PaymentMethod(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        null=False,
        blank=False,
        max_length=120,
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'payment_method'
        verbose_name = 'Payment Method'
        verbose_name_plural = 'Payment Methods'


class Genre(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        max_length=120,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'genre'
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class Movie(ModelBase):
    name = models.CharField(
        db_column='tx_name',
        null=False,
        blank=False,
        max_length=120,
    )

    parental_rating = models.IntegerField(
        db_column='nb_parental_rating',
        null=False,
        blank=False,
    )

    genre = models.ManyToManyField(
        Genre,
        through='MovieGenre',
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'movie'
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'


class MovieGenre(ModelBase):
    movie = models.ForeignKey(
        Movie,
        db_column='id_movie',
        on_delete=models.PROTECT,
        related_name="movie_genres",
        null=False,
        blank=False,
    )
    genre = models.ForeignKey(
        Genre,
        db_column='id_genre',
        on_delete=models.PROTECT,
        related_name="genre_movies",
        null=False,
        blank=False,
    )

    def __str__(self):
        return f"{self.movie.name} - {self.genre.name}"

    class Meta:
        db_table = 'movie_genre'
        verbose_name = 'Movie Genre'
        verbose_name_plural = 'Movie Genres'


class Room(ModelBase):
    class Type(models.IntegerChoices):
        NORMAL = 1
        VIP = 2
        THREE_DIMENSIONAL = 3

    room_type = models.IntegerField(
        db_column='cs_room_type',
        choices=Type.choices,
        default=Type.NORMAL,
        null=False,
        blank=False,
    )
    room_number = models.CharField(
        db_column='tx_room_number',
        max_length=40,
        null=False,
        blank=False,
    )
    seat_capacity = models.IntegerField(
        db_column='nr_seat_capacity',
        null=False,
        blank=False,
    )

    def __str__(self):
        return f"Room {self.room_number} ({self.get_room_type_display()})"

    class Meta:
        db_table = 'room'
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'


class Session(ModelBase):
    date_time = models.DateTimeField(
        db_column='dt_date_time',
        null=False,
        blank=False,
    )
    movie = models.ForeignKey(
        Movie,
        db_column='id_movie',
        on_delete=models.PROTECT,
        related_name="sessions",
        null=False,
        blank=False,
    )
    room = models.ForeignKey(
        Room,
        db_column='id_room',
        on_delete=models.CASCADE,
        related_name="sessions",
        null=False,
        blank=False,
    )

    def __str__(self):
        return f"{self.movie.name} - {self.date_time.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        db_table = 'session'
        verbose_name = 'Session'
        verbose_name_plural = 'Sessions'


class Purchase(ModelBase):
    total_value = models.FloatField(
        db_column='nb_total_value',
        null=True,
        blank=True,
    )
    customer = models.ForeignKey(
        Customer,
        db_column='id_customer',
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        related_name="purchases",
    )
    payment_method = models.ForeignKey(
        PaymentMethod,
        db_column='id_payment_method',
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        related_name="purchases",
    )

    def __str__(self):
        return f"Purchase {self.id} - {self.customer.name}"

    class Meta:
        db_table = 'purchase'
        verbose_name = 'Purchase'
        verbose_name_plural = 'Purchases'


class Ticket(ModelBase):
    value = models.FloatField(
        db_column='nb_value',
        null=False,
        blank=False,
    )
    seat_position = models.CharField(
        db_column='tx_seat_position',
        max_length=40,
        null=False,
        blank=False,
    )
    purchase = models.ForeignKey(
        Purchase,
        db_column='id_purchase',
        on_delete=models.PROTECT,
        related_name="tickets",
        null=True,
        blank=False,
    )
    session = models.ForeignKey(
        Session,
        db_column='id_session',
        on_delete=models.PROTECT,
        related_name="tickets",
        null=False,
        blank=False,
    )

    def __str__(self):
        return f"Ticket {self.id} - Session {self.session.id}"

    class Meta:
        db_table = 'ticket'
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'


class SeatMap(ModelBase):
    seats_data = models.JSONField(
        db_column='js_seats_data',
        null=False,
        blank=False,
    )
    session = models.ForeignKey(
        Session,
        db_column='id_session',
        on_delete=models.CASCADE,
        related_name="seat_maps",
        null=False,
        blank=False,
    )

    def __str__(self):
        return f"Seat Map - Session {self.session.id}"

    class Meta:
        db_table = 'seat_map'
        verbose_name = 'Seat Map'
        verbose_name_plural = 'Seat Maps'

class RoomMap(ModelBase):
    seats_layout = models.JSONField(
        db_column='js_seats_layout',
        null=True,
        blank=True,
    )
    room = models.ForeignKey(
        Room,
        db_column='id_room',
        on_delete=models.CASCADE,
        related_name="room_maps",
        null=False,
        blank=False,
    )

    def __str__(self):
        return f"Mapa da Sala {self.room.room_number}"

    class Meta:
        db_table = 'room_map'
        verbose_name = 'Room Map'
        verbose_name_plural = 'Room Maps'


var = {
    [
        [0, 0, 2, 0, 0, 1, 0,2, 0, 0],
        [0, 0, 2, 0, 0, 0, 0,2, 0, 0],
        [0, 0, 2, 0, 0, 0, 0,2, 0, 0],
        [0, 0, 2, 0, 0, 0, 0,2, 0, 0]
    ]
}
vago = 0
ocupado =1
vazio =2
disabilitado = 3
pcd_vago = 4
pcd_ocupado = 5
