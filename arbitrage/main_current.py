from django.shortcuts import render
from django.http import HttpResponse
import arbitrage.CoinData.CoinDataManager as cdm
def main(request):
    CDM = cdm.CoinDataManager()
    return HttpResponse("'BTCUSDT': {btc}, 'ETHUSDT' : {eth}, 'RATIO' : {ratio}".format(btc=CDM.getBTC(),eth=CDM.getETH()),ratio=CDM.ratio)