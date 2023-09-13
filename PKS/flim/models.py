from django.contrib.auth.models import User
    
from django.db import models

# Create your models here.

class Operator(models.Model):
    Operator_id=models.PositiveIntegerField()
    Operator_name = models.CharField(max_length=255)
    Contact_number = models.CharField(max_length=20)
    Address = models.CharField(max_length=255)

class Bus(models.Model):
    Bus_id=models.PositiveIntegerField()
    Bus_name = models.CharField(max_length=255)
    Total_seats = models.PositiveIntegerField()
    Bus_type = models.CharField(max_length=255)
    Operator_name = models.ForeignKey(Operator, on_delete=models.CASCADE)


class Route(models.Model):
    Route_id=models.PositiveIntegerField()
    Source_city = models.CharField(max_length=255)
    Destination_city = models.CharField(max_length=255)
    Distance = models.DecimalField(max_digits=10, decimal_places=2)

class BusSchedule(models.Model):
    Schedule_id=models.PositiveIntegerField()
    Bus_id = models.ForeignKey(Bus, on_delete=models.CASCADE)
    Route_id = models.ForeignKey(Route, on_delete=models.CASCADE)
    Departure_time = models.DateTimeField()
    Arrival_time = models.DateTimeField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Available_seats = models.PositiveIntegerField()


class Booking(models.Model):
    Booking_id=models.PositiveIntegerField()
    User_id = models.IntegerField()
    Schedule_id = models.ForeignKey(BusSchedule, on_delete=models.CASCADE)
    Booking_date = models.DateTimeField(auto_now_add=True)
    No_of_tickets = models.PositiveIntegerField()



class Payment(models.Model):
    Payment_id=models.PositiveIntegerField()
    Booking_id = models.ForeignKey(Booking, on_delete=models.CASCADE)
    Payment_date = models.DateTimeField(auto_now_add=True)
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    Payment_status = models.CharField(max_length=255)


class SeatReservation(models.Model):
    Reservation_id=models.PositiveIntegerField()
    Schedule_id = models.ForeignKey(BusSchedule, on_delete=models.CASCADE)
    Seat_number = models.PositiveIntegerField()
    Is_reserved = models.BooleanField(default=False)


class ReviewAndRating(models.Model):
    User_id = models.ForeignKey(Booking, on_delete=models.CASCADE)
    Bus_id = models.ForeignKey(Bus, on_delete=models.CASCADE)
    Rating = models.PositiveIntegerField()
    Review_text = models.TextField()
    Review_date = models.DateTimeField(auto_now_add=True)