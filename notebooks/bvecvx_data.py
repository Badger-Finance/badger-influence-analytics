from decimal import Decimal
from typing import Dict
from typing import List


def get_rows_from_data(data: Dict) -> List[List[Decimal]]:
    return [[
        data['total_cvx_sold_in_$'], data['total_badger_sold_in_$'],
        data['amount_cvx'],
        data['amount_badger'], data['$/vlCVX for total votes'],
        data['$/vlCVX without badgerwbtc'], ]
    ]


VOTING_DATA_R23 = {
    'round': "21st of July",
    'total_cvx_sold_in_$': Decimal('106428.420'),
    'total_badger_sold_in_$': Decimal('40662.305'),
    'amount_cvx': Decimal('16893.400'),
    'amount_badger': Decimal('10453.035'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('3.890'),
    'cvx_price_at_the_moment_of_sale_in_$': Decimal('6.300'),
    '$/vlCVX for total votes': Decimal('0.060'),
    '$/vlCVX without badgerwbtc': Decimal('0.066')
}

BRIBES_HARVESTED_DATA_R23 = {"frax": Decimal(228333.4003595493159628450234),
                             "2pool-frax": Decimal(139675.8051593709082650805046),
                             "dola": Decimal(617441.7348492212164141448451),
                             "alusd": Decimal(563262.0933380010783766220852),
                             "aleth": Decimal(565724.8043157838119237822106),
                             "fpifrax": Decimal(112585.9844037608392463191238),
                             "f-badgerwbtc": Decimal(235687.1553570462402634102000)}

VOTING_DATA_R24 = {
    'round': "4th August",
    'total_cvx_sold_in_$': Decimal('142446.574'),
    'total_badger_sold_in_$': Decimal('53399.085'),
    'amount_cvx': Decimal('20091.195'), 'amount_badger': Decimal('10288.841'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('5.190'),
    'cvx_price_at_the_moment_of_sale_in_$': Decimal('7.090'),
    '$/vlCVX for total votes': Decimal('0.080'),
    '$/vlCVX without badgerwbtc': Decimal('0.088')}

BRIBES_HARVESTED_DATA_R24 = {"frax": Decimal(14614.19678362758295371181277),
                             "2pool-frax": Decimal(499048.4835809215986880728746),
                             "fpifrax": Decimal(349803.5770423613211133454789),
                             "eursusd": Decimal(611593.8229378686932526214025),
                             "alusd": Decimal(366930.0417271141398514289506),
                             "aleth": Decimal(374269.9551634367764534647241),
                             "f-badgerwbtc": Decimal(230377.7348722152858835977500)}

VOTING_DATA_R25 = {
    'round': "18th August",
    'total_cvx_sold_in_$': Decimal('104711.127'),
    'total_badger_sold_in_$': Decimal('39537.871'),
    'amount_cvx': Decimal('19426.9252'),
    'amount_badger': Decimal('10111.9874'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('3.91'),
    'cvx_price_at_the_moment_of_sale_in_$': Decimal('5.39'),
    '$/vlCVX for total votes': Decimal('0.0583'),
    '$/vlCVX without badgerwbtc': Decimal('0.0643')
}

BRIBES_HARVESTED_DATA_R25 = {"2pool-frax": Decimal(79413.61100609367262977928944),
                             "frax": Decimal(133831.2485283798421340128355),
                             "fpifrax": Decimal(606275.2833809552228298586112),
                             "tusd": Decimal(541963.5299455261134157644223),
                             "alusd": Decimal(430654.7259226680394298321723),
                             "aleth": Decimal(450442.9577489539192495534612),
                             "f-badgerwbtc": Decimal(230947.6217531580304679192000)}

VOTING_DATASETS = [VOTING_DATA_R23, VOTING_DATA_R24, VOTING_DATA_R25]
