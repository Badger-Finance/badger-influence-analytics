from decimal import Decimal
from typing import Dict
from typing import List

VOTING_DATA_R23 = {'total_cvx_sold_in_$': Decimal('106428.420'),
                   'total_badger_sold_in_$': Decimal('40662.305'),
                   'amount_cvx': Decimal('16893.400'),
                   'amount_badger': Decimal('10453.035'),
                   'badger_price_at_the_moment_of_sale_in_$': Decimal('3.890'),
                   'cvx_price_at_the_moment_of_sale_in_$': Decimal('6.300'),
                   '$/vlCVX for total votes': Decimal('0.060'),
                   '$/vlCVX without badgerwbtc': Decimal('0.066')}

BRIBES_HARVESTED_DATA_R23 = {"frax": Decimal(228333.4003595493159628450234),
                             "2pool-frax": Decimal(139675.8051593709082650805046),
                             "dola": Decimal(617441.7348492212164141448451),
                             "alusd": Decimal(563262.0933380010783766220852),
                             "aleth": Decimal(565724.8043157838119237822106),
                             "fpifrax": Decimal(112585.9844037608392463191238),
                             "f-badgerwbtc": Decimal(235687.1553570462402634102000)}


def get_rows_from_data(data: Dict) -> List[List[Decimal]]:
    return [[
        data['total_cvx_sold_in_$'], data['total_badger_sold_in_$'],
        data['amount_cvx'],
        data['amount_badger'], data['$/vlCVX for total votes'],
        data['$/vlCVX without badgerwbtc'], ]
    ]
