
from enum import Enum, unique
import requests

BASE_URL = "https://min-api.cryptocompare.com/data/generateAvg?fsym=%s&tsym=%s&markets=%s"

@unique
class Markets(Enum):
    Paribu = 'Paribu'
    Koinim = 'Koinim'
    Cexio = 'Cexio'
    Bitstamp = 'Bitstamp'
    Bitfinex = 'Bitfinex'
    Poloniex = 'Poloniex'
    BTCE = 'BTCE'
    OKCoin = 'OKCoin'
    Coinbase = 'Coinbase'
    Kraken = 'Kraken'

class Ticker:
    '''Ticker api for some popular markets.'''
    def __init__(self):
        self.market = None
        self.couple = None

    @property
    def pair(self):
        return self.couple
    
    @pair.setter
    def pair(self, value):
        self.couple = value

    @property
    def market(self):
        return self.market
    
    @market.setter
    def market(self, value):
        self.market = value

    def ticker(self):
        couple = self.couple.split('/')
        request_url = BASE_URL % (couple[0], couple[1], self.market.value)
        result = self.__api_call(request_url)

        try:
            result = {
                'price': result['DISPLAY']['PRICE'],
                'volume24h': result['DISPLAY']['VOLUME24HOUR'],
                'open24h': result['DISPLAY']['OPEN24HOUR'],
                'high24h': result['DISPLAY']['HIGH24HOUR'],
                'low24h': result['DISPLAY']['LOW24HOUR'],
                'change24h': result['DISPLAY']['CHANGE24HOUR']
            }
        except KeyError:
            return None

        return result

    def __api_call(self, uri):
        result = requests.get(uri).json()
        return result