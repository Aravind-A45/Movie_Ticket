from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name="index"),
  path("operator/", views.operator, name='operator'),
  path("bus_details/", views.bus_details, name='bus_details'),
  path("route_details/", views.route_details, name='route_details'),
  path("bus_schedule/", views.bus_schedule, name='bus_schedule'),
  path("book/", views.book, name='book'),
  path("pay/", views.pay, name='pay'),
  path("reser/", views.reser, name='reser'),
  path("review/", views.review, name='review'),
  path("login/", views.login, name='login'),
  path("home/", views.home, name='home'),

]