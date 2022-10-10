from typing import Dict
from typing import List
from typing import Tuple

import requests
from pycoingecko import CoinGeckoAPI

from notebooks.bribes_research.constants import DASHBOARD_URL

CURRENCY_USD = "usd"
AURA_TOKEN_CG_ALIAS = "aura-finance"
BALANCER_TOKEN_CG_ALIAS = "balancer"
BADGER_TOKEN_CG_ALIAS = "badger-dao"
TOKENS_LIST = [
    AURA_TOKEN_CG_ALIAS, BADGER_TOKEN_CG_ALIAS, BADGER_TOKEN_CG_ALIAS
]


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


"""
This lambda gets token prices for TOKENS_LIST 
"""
get_preset_token_prices = lambda: fetch_token_prices(TOKENS_LIST)


def get_dollar_per_vl_asset_for_snapshot(snapshot_id: str) -> float:
    aura_dash = requests.post(DASHBOARD_URL, json={"id": "bribes-overview-aura"}).json()
    dollar_per_vl_asset = None
    for epoch in aura_dash['dashboard']['epochs']:
        if epoch['proposal'] == snapshot_id:
            dollar_per_vl_asset = epoch['dollarPerVlAsset']
    if not dollar_per_vl_asset:
        raise ValueError(f"Cannot obtain dollar per vlAURA for snapshot id: {snapshot_id}")
    return dollar_per_vl_asset
