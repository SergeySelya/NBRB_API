from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from .mixins import LoggingMixin
import datetime


class ExchangeRateList(LoggingMixin,APIView):
    lookup_field = "date"

    # returns a response indicating that the data loading was completed correctly
    def get(self,request,date,format=None):
        url = f'https://api.nbrb.by/exrates/rates?ondate={date}&periodicity=0'
        return Response(status=status.HTTP_200_OK)

class ExchangeRate(LoggingMixin,APIView):
    lookup_fields = ("curr_name","date")

    #returns the exchange rate of the specified currency on the specified date
    def get(self, request, curr_name,date, format=None):
        url = f'https://api.nbrb.by/exrates/rates/{curr_name}?ondate={date}&parammode=2'
        response = requests.get(url)
        data = response.json()

        # add field about changing rate from last day
        datetime_object =  datetime.datetime.strptime(date, '%Y-%m-%d').date()
        last_day = str(datetime_object - datetime.timedelta(days=1))
        response_rate_yst = requests.get(f'https://api.nbrb.by/exrates/rates/{curr_name}?ondate={last_day}&parammode=2')
        data_rate_yst = response_rate_yst.json()

        # calculate difference between rate from last day
        diff_rate = data['Cur_OfficialRate'] - data_rate_yst['Cur_OfficialRate']
        if diff_rate > 0:
            data.update({"diff_rate": f'{diff_rate} - rate increased'})
        elif diff_rate < 0:
            data.update({"diff_rate": f'{diff_rate} - rate fell'})
        else :
            data.update({"diff_rate": f'{diff_rate} - rate not change'})

        return Response(data, status=status.HTTP_200_OK)


