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


VOTING_ROUNDS = [VOTING_DATA_R6]
