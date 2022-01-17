from curses import meta
import imp
from statistics import quantiles
from rest_framework.views import APIView
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.response import Response
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache
from django.conf import settings
from .models import Quote
from .serializers import QuoteSerializer
import requests

class QuoteView(APIView):
    permission_classes = [HasAPIKey]

    @method_decorator(cache_page(60*60))
    def get(self, request):
        latestQuote = Quote.objects.last()
        # print(latestQuote)
        serializer = QuoteSerializer(latestQuote, many=False)
        # print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        res  = get_exchange_rate()
        return Response(res)

def get_exchange_rate():
    print(settings.ALPAHVANTAGE_API_KEY)
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey={settings.ALPAHVANTAGE_API_KEY}'
    r = requests.get(url)
    data = r.json()
    data = list(data.values())[0]
    data_value_list = list(data.values())
    quote_json = {
        'from_currency_code': data_value_list[0],
        'from_currency_name': data_value_list[1],
        'to_currency_code': data_value_list[2],
        'to_currency_name': data_value_list[3],
        'exchange_rate': data_value_list[4],
        'last_refreshed': data_value_list[5],
        'time_zone': data_value_list[6],
        'bid_price': data_value_list[7],
        'ask_price': data_value_list[8],
    }
    serializer = QuoteSerializer(data = quote_json)
    if serializer.is_valid():
        serializer.save()
        cache.clear()
    print(serializer.errors)
    return serializer.data