import json
import requests
from config import keys

class ConvertionExceptions(Exception):
    pass

class Converter:
    @staticmethod
    def get_price(quote:str, base:str, amount:str):
        if quote == base:
            raise ConvertionExceptions(f'Невозможно перевести одинаковые валюты{base}')

        try:
            quote_thicker = keys[quote]
        except KeyError:
            raise ConvertionExceptions(f'Не удалось обработать валюту {quote}')

        try:
            base_thicker = keys[base]
        except KeyError:
            raise ConvertionExceptions(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExceptions(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_thicker}&tsyms={base_thicker}')
        total_base = amount * json.loads(r.content)[keys[base]]

        return total_base
