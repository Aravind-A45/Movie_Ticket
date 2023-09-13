from django.shortcuts import render
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

# Create your views here.

def login(request):
  return render(request, "login.html")

def home(request):
  return render(request, "index.html", {'name':"Red Bus App"})
    
def index(request):
  return render(request, "index.html", {'name':"Red Bus App"})

def operator(request):
  if request.method == 'POST':
    opid = request.POST.get('Opid')
    opn = request.POST.get('Opn')
    cno = request.POST.get('Cno')
    adr = request.POST.get('Adr')
    Operator.objects.create(Operator_id = opid, Operator_name = opn, Contact_number = cno, Address = adr)
    return render(request, "operator.html")
  else:
    return render(request, "operator.html")

def bus_details(request):
  if request.method == 'POST':
    bid = request.POST.get('Bid')
    bn = request.POST.get('Bn')
    tct = request.POST.get('Tct')
    btype = request.POST.get('Btype')
    b = request.POST.get('Operator_name')
    opn = Operator.objects.get(Operator_name = b)
    Bus.objects.create(Bus_id = bid, Bus_name = bn, Total_seats = tct, Bus_type = btype, Operator_name = Operator_name)
    return render(request, "bus_details.html")
  else:
    return render(request, "bus_details.html")

def route_details(request):
  if request.method == 'POST':
    rid = request.POST.get('Rid')
    scty = request.POST.get('Scty')
    dcty = request.POST.get('Dcty')
    dis = request.POST.get('Dis')
    Route.objects.create(Route_id = rid, Source_city = scty, Destination_city = dcty, Distance = dis)
    return render(request, "route_details.html")
  else:
    return render(request, "route_details.html")

def bus_schedule(request):
  if request.method == 'POST':
    sid = request.POST.get('Sid')
    bid = Bus.objects.get(Bus_id = Bid)
    rid = Route.objects.get(Route_id = Rid)
    dtime = request.POST.get('Dtime')
    atime = request.POST.get('Atime')
    pr = request.POST.get('Pr')
    aseat = request.POST.get('Aseat')
    BusSchedule.objects.create(Schedule_id = sid, Bus_id = bid, Route_id = rid, Departure_time = dtime, Arrival_time = atime, Price = pr, Available_seats = aseat)
    return render(request, "bus_schedule.html")
  else:
    return render(request, "bus_schedule.html")

def book(request):
  if request.method == 'POST':
    bookid = request.POST.get('Bookid')
    uid = request.POST.get('Uid')
    sid = BusSchedule.objects.get(Schedule_id = Sid)
    bdate = request.POST.get('Bdate')
    no_tic = request.POST.get('No_tic')
    Booking.objects.create(Booking_id = Bookid, User_id = Uid, Schedule_id = Sid, Booking_date = Bdate, No_of_tickets = No_tic)
    return render(request, "book.html")
  else:
    return render(request, "book.html")

def pay(request):
  if request.method == 'POST':
    payid = request.POST.get('Payid')
    bookid = Booking.objects.get(Booking_id = Bookid)
    pdate = request.POST.get('Pdate')
    amt = request.POST.get('Amt')
    pay_sts = request.POST.get('Pay_sts')
    Payment.objects.create(Payment_id = Payid, Booking_id = Bid, Payment_date = Pdate, Amount = Amt, Payment_status = Pay_sts)
    return render(request, "pay.html")
  else:
    return render(request, "pay.html")

def reser(request):
  if request.method == 'POST':
    resid = request.POST.get('Resid')
    sid = Booking.objects.get(Schedule_id = Sid)
    sno = request.POST.get('Sno')
    isr = request.POST.get('Isr')
    SeatReservation.objects.create(Reservation_id = Resid, Schedule_id = Sid, Seat_number = Sno, Is_reserved = Isr)
    return render(request, "reser.html")
  else:
    return render(request, "reser.html")

def review(request):
  if request.method == 'POST':
    uid = Booking.objects.get(User_id = Uid)
    bid = Booking.objects.get(Bus_id = Bid)
    rate = request.POST.get('Rate')
    rtext = request.POST.get('Rtext')
    rdate = request.POST.get('Rdate')
    ReviewAndRating.objects.create(User_id = Uid, Bus_id = Bid, Rating = Rate, Review_text = Rtext, Review_date = Rdate)
    return render(request, "review.html")
  else:
    return render(request, "review.html")