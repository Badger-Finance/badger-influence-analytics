from typing import Dict
from typing import List

from pycoingecko import CoinGeckoAPI

CURRENCY_USD = "usd"


def fetch_token_prices(tokens: List[str]) -> Dict:
    gecko = CoinGeckoAPI()
    prices = gecko.get_price(ids=",".join(tokens), vs_currencies=CURRENCY_USD)
    return prices
