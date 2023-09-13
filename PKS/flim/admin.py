from django.contrib import admin
from . models import Operator
from . models import Bus
from . models import Route
from . models import BusSchedule
from . models import Booking
from . models import Payment
from . models import SeatReservation
from . models import ReviewAndRating

# Register your models here.

admin.site.register(Operator)
admin.site.register(Bus)
admin.site.register(Route)
admin.site.register(BusSchedule)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(SeatReservation)
admin.site.register(ReviewAndRating)