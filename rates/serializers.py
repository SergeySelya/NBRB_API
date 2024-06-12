from rest_framework import serializers
from .models import ExchangeRate

class ExchangeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRate
        fields = ["cur_id", "date", "cur_abbreviation","cur_scale", "cur_name", "cur_officialRate"]