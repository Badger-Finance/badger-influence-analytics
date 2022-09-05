from typing import Dict
from typing import List
from typing import Tuple

from pycoingecko import CoinGeckoAPI

CURRENCY_USD = "usd"


def fetch_token_prices(tokens: List[str]) -> Dict:
    gecko = CoinGeckoAPI()
    prices = gecko.get_price(ids=",".join(tokens), vs_currencies=CURRENCY_USD)
    return prices


def calculate_metrics(
        badger_bribe: float, total_platform_bribes: float, dollar_spent_on_bribes: float
) -> Tuple[float, float]:
    dilution = badger_bribe / total_platform_bribes * 100
    dollar_in_out = (100 - dilution) * dollar_spent_on_bribes
    return dilution, dollar_in_out
