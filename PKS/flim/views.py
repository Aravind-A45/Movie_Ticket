from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Operator
from .models import Bus
from .models import Route
from .models import BusSchedule
from .models import Booking
from .models import Payment
from .models import SeatReservation
from .models import ReviewAndRating
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def login(request):
  if request.method == 'POST':
    form = UserCreationForm()
    if form.is_valid():
        form.save()
        return redirect('home')
  else:
    form = UserCreationForm()
  return render(request, "login.html", {'form' : form})

def home(request):
  return render(request, "index.html", {'name':"Red Bus App"})
    
def index(request):
  return render(request, "index.html", {'name':"Red Bus App"})

def operator(request):
  if request.method == 'POST':
    opid = request.POST.get('Opid')
    Operator_name = request.POST.get('Operator_name')
    cno = request.POST.get('Cno')
    adr = request.POST.get('Adr')
    Operator.objects.create(Operator_id = opid, Operator_name = Operator_name, Contact_number = cno, Address = adr)
    return render(request, "operator.html")
  else:
    return render(request, "operator.html")

def bus_details(request):
  if request.method == 'POST': 
    Bus_id = request.POST.get('Bus_id')
    bn = request.POST.get('Bn')
    tct = request.POST.get('Tct')
    btype = request.POST.get('Btype')
    Operator_name = Operator.objects.first()
    Bus.objects.create(Bus_id = Bus_id, Bus_name = bn, Total_seats = tct, Bus_type = btype, Operator_name = Operator_name)
    return render(request, "bus_details.html")
  else:
    return render(request, "bus_details.html")

def route_details(request):
  if request.method == 'POST':
    Route_id= request.POST.get('Route_id')
    scty = request.POST.get('Scty')
    dcty = request.POST.get('Dcty')
    dis = request.POST.get('Dis')
    Route.objects.create(Route_id = Route_id, Source_city = scty, Destination_city = dcty, Distance = dis)
    return render(request, "route_details.html")
  else:
    return render(request, "route_details.html")

def bus_schedule(request):
  if request.method == 'POST':
    Schedule_id = request.POST.get('Schedule_id')
    Bus_id = Bus.objects.first()
    Route_id = Route.objects.first()
    Departure_time = request.POST.get('Departure_time')
    Arrival_time = request.POST.get('Arrival_time')
    Price = request.POST.get('Price')
    Available_seats = request.POST.get('Available_seats')
    BusSchedule.objects.create(Schedule_id = Schedule_id , Bus_id = Bus_id, Route_id = Route_id, Departure_time = Departure_time, Arrival_time = Arrival_time , Price =Price, Available_seats =Available_seats)
    return render(request, "bus_schedule.html")
  else:
    return render(request, "bus_schedule.html")

def book(request):
  if request.method == 'POST':
    Booking_id= request.POST.get('Booking_id')
    User_id = request.POST.get('User_id')
    Schedule_id= BusSchedule.objects.first()
    Booking_date = request.POST.get('Booking_date')
    No_of_tickets = request.POST.get('No_of_tickets')
    Booking.objects.create(Booking_id = Booking_id, User_id = User_id, Schedule_id = Schedule_id , Booking_date = Booking_date, No_of_tickets = No_of_tickets)
    return render(request, "book.html")
  else:
    return render(request, "book.html")

def pay(request):
  if request.method == 'POST':
    Payment_id = request.POST.get('Payment_id')
    Booking_id = Booking.objects.first()
    Payment_date = request.POST.get('Payment_date')
    Amount  = request.POST.get('Amount')
    Payment_status = request.POST.get('Payment_status')
    Payment.objects.create(Payment_id = Payment_id , Booking_id = Booking_id, Payment_date = Payment_date, Amount = Amount, Payment_status = Payment_status)
    return render(request, "pay.html")
  else:
    return render(request, "pay.html")

def reser(request):
  if request.method == 'POST':
    Reservation_id= request.POST.get('Reservation_id')
    Schedule_id = BusSchedule.objects.first()
    Seat_number= request.POST.get('Seat_number')
    Is_reserved = request.POST.get('Is_reserved')
    SeatReservation.objects.create(Reservation_id = Reservation_id , Schedule_id = Schedule_id, Seat_number = Seat_number, Is_reserved = Is_reserved)
    return render(request, "reser.html")
  else:
    return render(request, "reser.html")

def review(request):
  if request.method == 'POST':
    Bus_id= Bus.objects.first()
    Rating  = request.POST.get('Rating')
    Review_text = request.POST.get('Review_text')
    Review_date  = request.POST.get('Review_date ')
    ReviewAndRating.objects.create( Bus_id = Bus_id, Rating = Rating , Review_text = Review_text, Review_date = Review_date)
    return render(request, "review.html")
  else:
    return render(request, "review.html")

