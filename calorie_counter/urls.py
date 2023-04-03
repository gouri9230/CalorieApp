from django.urls import path
from . import views 
from .views import MealCreateView

urlpatterns = [
    path('', views.home, name='home' ),
    path('home/', views.home, name = 'home'),
    path('sign-up/', views.sign_up, name = 'sign-up'),
    path('meal/create/', MealCreateView.as_view(), name='meal_create'),
    path('queryresults/', views.queryresults, name = "queryresults"),
    path('querysearch/', views.querysearch, name = "querysearch"),
    path('bmi-cal/', views.bmi_cal, name = "bmi_cal"),
]