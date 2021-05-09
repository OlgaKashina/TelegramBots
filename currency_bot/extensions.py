import requests
import json
from config import keys, API_KEY, website


class APIException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):

        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote.lower()]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base.lower()]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        try:
            amount = int(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        r_quote = requests.get(f'{website}?access_key={API_KEY}&symbols{quote_ticker}')
        r_base = requests.get(f'{website}?access_key={API_KEY}&symbols{base_ticker}')

        if base == "EUR":
            total_base = json.loads(r.content)['rates'][quote_ticker] * amount

        else:
            A = json.loads(r_base.content)['rates'][base_ticker]
            B = json.loads(r_quote.content)['rates'][quote_ticker]

        total_base = (B/A) * amount

        return round(total_base, 2)
