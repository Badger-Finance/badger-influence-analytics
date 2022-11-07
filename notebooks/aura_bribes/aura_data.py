from decimal import Decimal
from typing import Dict
from typing import List


def get_rows_from_data(data: Dict) -> List[Decimal]:
    return [
        data['round'], data['total_graviaura_bought_in_$'], data['total_badger_bought_in_$'],
        data['amount_graviaura_bought'],
        data['amount_badger_bought'], data['$/vlAURA for total votes'],
        data['$/vlAURA without pools'], data['llama_vlaura'],
    ]


VOTING_DATA_R6 = {
    'round': "1st September 2022",
    'total_graviaura_bought_in_$': Decimal('26371.21'),
    'total_badger_bought_in_$': Decimal('8983.14'),
    'amount_graviaura_bought': Decimal('8618.04'),
    'amount_badger_bought': Decimal('2133.76'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('4.21'),
    'graviaura_price_at_the_moment_of_sale_in_$': Decimal('3.06'),
    '$/vlAURA for total votes': Decimal('0.04'),
    '$/vlAURA without pools': Decimal('0.069'),
    'llama_vlaura': Decimal('0.08562'),
}

VOTING_DATA_R7 = {
    'round': "15th September 2022",
    'total_graviaura_bought_in_$': Decimal('25066.2'),
    'total_badger_bought_in_$': Decimal('8618.6'),
    'amount_graviaura_bought': Decimal('12227.39'),
    'amount_badger_bought': Decimal('2427.75'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('3.55'),
    'graviaura_price_at_the_moment_of_sale_in_$': Decimal('2.05'),
    '$/vlAURA for total votes': Decimal('0.037'),
    '$/vlAURA without pools': Decimal('0.064'),
    'llama_vlaura': Decimal('0.066'),
}

# For R8 voter voted 10% for badger-wbtc pool and harvested bribes that weren't sold
# so they don't take part in the calculations
VOTING_DATA_R8 = {
    'round': "29th September 2022",
    'total_graviaura_bought_in_$': Decimal('22640.234'),
    'total_badger_bought_in_$': Decimal('7509.109'),
    'amount_graviaura_bought': Decimal('11853.53'),
    'amount_badger_bought': Decimal('2013.17'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('3.73'),
    'graviaura_price_at_the_moment_of_sale_in_$': Decimal(
        '1.91'),
    '$/vlAURA for total votes': Decimal('0.033'),
    '$/vlAURA without pools': Decimal('0.064'),
    'llama_vlaura': Decimal('0.063'),
}

VOTING_DATA_R9 = {
    'round': "13th October 2022",
    'total_graviaura_bought_in_$': Decimal('16943.89'),
    'total_badger_bought_in_$': Decimal('5084.28'),
    'amount_graviaura_bought': Decimal('6915.87'),
    'amount_badger_bought': Decimal('1540.69'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('3.3'),
    'graviaura_price_at_the_moment_of_sale_in_$': Decimal('2.45'),
    '$/vlAURA for total votes': Decimal('0.0273'),
    '$/vlAURA without pools': Decimal('0.0600'),
    'llama_vlaura': Decimal('0.059'),
}

VOTING_DATA_R10 = {
    'round': "27th October 2022",
    'total_graviaura_bought_in_$': Decimal('16959.24'),
    'total_badger_bought_in_$': Decimal('5913.99'),
    'amount_graviaura_bought': Decimal('5929.80'),
    'amount_badger_bought': Decimal('1661.23'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('3.56'),
    'graviaura_price_at_the_moment_of_sale_in_$': Decimal('2.85'),
    '$/vlAURA for total votes': Decimal('0.036'),
    '$/vlAURA without pools': Decimal('0.067'),
    'llama_vlaura': Decimal('0.066'),
}

VOTING_ROUNDS = [VOTING_DATA_R6, VOTING_DATA_R7, VOTING_DATA_R8, VOTING_DATA_R9, VOTING_DATA_R10]
