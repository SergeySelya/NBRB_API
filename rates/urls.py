from django.urls import path
from . import views

urlpatterns = [
    path("rateView/<str:date>/", views.ExchangeRateList.as_view(), name='ExchangeRate view'),
    path("rateView/<str:date>/<str:curr_name>/", views.ExchangeRate.as_view(), name='ExchangeRate view'),
]
