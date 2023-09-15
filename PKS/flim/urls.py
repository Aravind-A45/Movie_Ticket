from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name="index"),
  path("login/operator/", views.operator, name='operator'),
  path("login/bus_details/", views.bus_details, name='bus_details'),
  path("login/route_details/", views.route_details, name='route_details'),
  path("login/bus_schedule/", views.bus_schedule, name='bus_schedule'),
  path("login/book/", views.book, name='book'),
  path("login/pay/", views.pay, name='pay'),
  path("login/reser/", views.reser, name='reser'),
  path("login/review/", views.review, name='review'),
  path("login/", views.login, name='login'),
  path("login/home/", views.home, name='home'),
  path("login/login", views.home, name='home'),

]