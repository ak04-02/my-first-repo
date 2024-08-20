from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns =[
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('menu/',views.menu,name="menu"),
    path('menu/<int:pk>',views.menu_item,name="menu_item"),
    path('book/',views.book,name="book"),
    path('bookings/',views.bookings,name="bookings"),
    path('reservations/',views.reservations,name="reservations"),
    path('api/menu', views.menuView.as_view()),  
    path('api/reservation', views.bookingView.as_view()),
    path('api=token-auth',obtain_auth_token,name="api_token_auth"),
]