from django.http import HttpResponse
import asyncio
from arbitrage.binanceBack.Ticker import recv_ticker
import arbitrage.CoinData.CoinDataManager as cdm
# Create your views here.


def mainpage(request):
    print("Run Ok")
    asyncio.run(recv_ticker())
    print("A")
    return HttpResponse(request,'arbitrage/main_current.html')
