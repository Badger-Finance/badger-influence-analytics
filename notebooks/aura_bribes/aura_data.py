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

VOTING_DATA_R11 = {
    'round': "10th November 2022",
    'total_graviaura_bought_in_$': Decimal('17305.1'),
    'total_badger_bought_in_$': Decimal('5682.33'),
    'amount_graviaura_bought': Decimal('8400.53'),
    'amount_badger_bought': Decimal('2309.89'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('2.46'),
    'graviaura_price_at_the_moment_of_sale_in_$': Decimal(
        '2.05'),
    '$/vlAURA for total votes': Decimal('0.034'),
    '$/vlAURA without pools': Decimal('0.0620'),
    'llama_vlaura': Decimal('0.0608'),
}

VOTING_DATA_R12 = {
    'round': "24th November 2022",
    'total_graviaura_bought_in_$': Decimal('14904.1'),
    'total_badger_bought_in_$': Decimal('5154.8'),
    'amount_graviaura_bought': Decimal('6133.4'),
    'amount_badger_bought': Decimal('1902.2'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('2.71'),
    'graviaura_price_at_the_moment_of_sale_in_$': Decimal('2.40'),
    '$/vlAURA for total votes': Decimal('0.03'),
    '$/vlAURA without pools': Decimal('0.048'),
    'llama_vlaura': Decimal('0.048'),
}

VOTING_DATA_R13 = {
    'round': "8th December 2022",
    'total_graviaura_bought_in_$': Decimal('10635.48'),
    'total_badger_bought_in_$': Decimal('3671.76'),
    'amount_graviaura_bought': Decimal('5291.28'),
    'amount_badger_bought': Decimal('1434.3'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('2.56'),
    'graviaura_price_at_the_moment_of_sale_in_$': Decimal('2.01'),
    '$/vlAURA for total votes': Decimal('0.026'),
    '$/vlAURA without pools': Decimal('0.042'),
    'llama_vlaura': Decimal('0.03698'),
}

VOTING_DATA_R14 = {
    'round': "22nd December 2022",
    'total_graviaura_bought_in_$': Decimal('4685.42'),
    'total_badger_bought_in_$': Decimal('3397.56'),
    'amount_graviaura_bought': Decimal('2342.71'),
    'amount_badger_bought': Decimal('1602.62'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('2.12'),
    'graviaura_price_at_the_moment_of_sale_in_$': Decimal('2'),
    '$/vlAURA for total votes': Decimal('0.011'),
    '$/vlAURA without pools': Decimal('0.016'),
    'llama_vlaura': Decimal('0.032'),
}

VOTING_DATA_R15 = {
    'round': "5th January 2023",
    'total_graviaura_bought_in_$': Decimal('12581.9'),
    'total_badger_bought_in_$': Decimal('3067.55'),
    'amount_graviaura_bought': Decimal('5719.07'),
    'amount_badger_bought': Decimal('1305.34'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('2.35'),
    'graviaura_price_at_the_moment_of_sale_in_$': Decimal('2.6'),
    '$/vlAURA for total votes': Decimal('0.027'),
    '$/vlAURA without pools': Decimal('0.037'),
    'llama_vlaura': Decimal('0.02629'),
}

VOTING_DATA_R16 = {
    'round': "19th January 2023",
    'total_graviaura_bought_in_$': Decimal('13314.44'),
    'total_badger_bought_in_$': Decimal('5887.4'),
    'amount_graviaura_bought': Decimal('6052.11'),
    'amount_badger_bought': Decimal('2009.34'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('2.93'),
    'graviaura_price_at_the_moment_of_sale_in_$': Decimal('2.87'),
    '$/vlAURA for total votes': Decimal('0.028'),
    '$/vlAURA without pools': Decimal('0.0383'),
    'llama_vlaura': Decimal('0.03795'),
}

VOTING_DATA_R17 = {
    'round': "2nd February 2023",
    'total_graviaura_bought_in_$': Decimal('13922.47'),
    'total_badger_bought_in_$': Decimal('6332.041'),
    'amount_graviaura_bought': Decimal('6328.26'),
    'amount_badger_bought': Decimal('1978.762'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('3.2'),
    'graviaura_price_at_the_moment_of_sale_in_$': Decimal('3.1'),
    '$/vlAURA for total votes': Decimal('0.029'),
    '$/vlAURA without pools': Decimal('0.040'),
    'llama_vlaura': Decimal('0.04351'),
}

VOTING_DATA_R18 = {
    'round': "16th February 2023",
    'total_graviaura_bought_in_$': Decimal('9513.6'),
    'total_badger_bought_in_$': Decimal('0'),
    'amount_graviaura_bought': Decimal('3109.026'),
    'amount_badger_bought': Decimal('0'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('0'),
    'graviaura_price_at_the_moment_of_sale_in_$': Decimal('3.25'),
    '$/vlAURA for total votes': Decimal('0.01'),
    '$/vlAURA without pools': Decimal('0.02'),
    'llama_vlaura': Decimal('0.06352'),
}

VOTING_DATA_R19 = {
    'round': "2nd March 2023",
    'total_graviaura_bought_in_$': Decimal('18477.24'),
    'total_badger_bought_in_$': Decimal('6288.42'),
    'amount_graviaura_bought': Decimal('5175.7'),
    'amount_badger_bought': Decimal('2051.01'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('3.06600000'),
    'graviaura_price_at_the_moment_of_sale_in_$': Decimal('3.57'),
    '$/vlAURA for total votes': Decimal('0.034'),
    '$/vlAURA without pools': Decimal('0.053'),
    'llama_vlaura': Decimal('0.05087'),
}

VOTING_DATA_R20 = {
    'round': "16th March 2023",
    'total_graviaura_bought_in_$': Decimal('12956.93'),
    'total_badger_bought_in_$': Decimal('4790.81'),
    'amount_graviaura_bought': Decimal('3810.86'),
    'amount_badger_bought': Decimal('1516.080'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('3.16'),
    'graviaura_price_at_the_moment_of_sale_in_$': Decimal('3.15'),
    '$/vlAURA for total votes': Decimal('0.034'),
    '$/vlAURA without pools': Decimal('0.057'),
    'llama_vlaura': Decimal('0.05638'),
}

VOTING_DATA_R21 = {
    '$/vlAURA for total votes': Decimal('0.03'),
    '$/vlAURA without pools': Decimal('0.05'),
    'amount_badger_bought': Decimal('2085.7'),
    'amount_graviaura_bought': Decimal('4068.33'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('2.6'),
    'graviaura_price_at_the_moment_of_sale_in_$': Decimal('3.1'),
    'total_badger_bought_in_$': Decimal('5420.6'),
    'total_graviaura_bought_in_$': Decimal('12611.81'),
    'round': '30th March 2023',
    'llama_vlaura': Decimal('0')
}

VOTING_DATA_R22 = {
    'round': '13th April 2023',
    'total_graviaura_bought_in_$': Decimal('16245.7'),
    'total_badger_bought_in_$': Decimal('5225.83'),
    'amount_graviaura_bought': Decimal('5507'),
    'amount_badger_bought': Decimal('1789.7'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('2.92'),
    'graviaura_price_at_the_moment_of_sale_in_$': Decimal(
        '2.92'),
    '$/vlAURA for total votes': Decimal('0.036'),
    '$/vlAURA without pools': Decimal('0.05974'),
    'llama_vlaura': Decimal('0.05968')
}

VOTING_DATA_R23 = {
    'round': '27th April 2023',
    'total_graviaura_bought_in_$': Decimal('15748.74'),
    'total_badger_bought_in_$': Decimal('5208.456'),
    'amount_graviaura_bought': Decimal('7094.027'),
    'amount_badger_bought': Decimal('1869.51'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('2.79'),
    'graviaura_price_at_the_moment_of_sale_in_$': Decimal('2.22'),
    '$/vlAURA for total votes': Decimal('0.026'),
    '$/vlAURA without pools': Decimal('0.0475'),
    'llama_vlaura': Decimal('0.046')
}

VOTING_DATA_R24 = {
    'round': '11th May 2023',
    'total_graviaura_bought_in_$': Decimal('10600.59'),
    'total_badger_bought_in_$': Decimal('3509.42'),
    'amount_graviaura_bought': Decimal('4608.95'),
    'amount_badger_bought': Decimal('1366.6'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('2.57'),
    'graviaura_price_at_the_moment_of_sale_in_$': Decimal(
        '1.99'),
    '$/vlAURA for total votes': Decimal('0.016'),
    '$/vlAURA without pools': Decimal('0.039'),
    'llama_vlaura': Decimal('0.03810'),
}

VOTING_DATA_R25 = {
    'round': '25th May 2023',
    'total_graviaura_bought_in_$': Decimal('7538.47'),
    'total_badger_bought_in_$': Decimal('2504.87'),
    'amount_graviaura_bought': Decimal('4074.85'),
    'amount_badger_bought': Decimal('998.75'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('2.51'),
    'graviaura_price_at_the_moment_of_sale_in_$': Decimal('1.85'),
    '$/vlAURA for total votes': Decimal('0.008'),
    '$/vlAURA without pools': Decimal('0.0325'),
    'llama_vlaura': Decimal('0.0315'),
}

VOTING_DATA_R26 = {
    'round': '8th June 2023',
    'total_graviaura_bought_in_$': Decimal('6862.7'),
    'total_badger_bought_in_$': Decimal('2258.21'),
    'amount_graviaura_bought': Decimal('4485.42'),
    'amount_badger_bought': Decimal('1163.43'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('1.94'),
    'graviaura_price_at_the_moment_of_sale_in_$': Decimal('1.53'),
    '$/vlAURA for total votes': Decimal('0.006'),
    '$/vlAURA without pools': Decimal('0.0281'),
    'llama_vlaura': Decimal('0.028'),
}

VOTING_DATA_R27 = {
    'round': '22nd June 2023',
    'total_graviaura_bought_in_$': Decimal('6143.478'), 
    'total_badger_bought_in_$': Decimal('2010.35'), 
    'amount_graviaura_bought': Decimal('3746.02'), 
    'amount_badger_bought': Decimal('913.38'), 
    'badger_price_at_the_moment_of_sale_in_$': Decimal('2.20'), 
    'graviaura_price_at_the_moment_of_sale_in_$': Decimal('1.64'), 
    '$/vlAURA for total votes': Decimal('0.0049'), 
    '$/vlAURA without pools': Decimal('0.033'),
    'llama_vlaura': Decimal('0.03424'),
}

VOTING_DATA_R28 = {
    'round': '11th July 2023',
    'total_graviaura_bought_in_$': Decimal('3582.85'), 
    'total_badger_bought_in_$': Decimal('1125.89'), 
    'amount_graviaura_bought': Decimal('2184.66'), 
    'amount_badger_bought': Decimal('527.104'), 
    'badger_price_at_the_moment_of_sale_in_$': Decimal('2.136'), 
    'graviaura_price_at_the_moment_of_sale_in_$': Decimal('1.64'), 
    '$/vlAURA for total votes': Decimal('0.00286'), 
    '$/vlAURA without pools': Decimal('0.027'),
    'llama_vlaura': Decimal('0.03424'),
}

VOTING_DATA_R29 = {
    'round': '26th July 2023',
    'total_graviaura_bought_in_$': Decimal('4065.11'), 
    'total_badger_bought_in_$': Decimal('1174.42'), 
    'amount_graviaura_bought': Decimal('2478.73'), 
    'amount_badger_bought': Decimal('562.73'), 
    'badger_price_at_the_moment_of_sale_in_$': Decimal('2.087'), 
    'graviaura_price_at_the_moment_of_sale_in_$': Decimal('1.64'), 
    '$/vlAURA for total votes': Decimal('0.0037'), 
    '$/vlAURA without pools': Decimal('0.0284'),
    'llama_vlaura': Decimal('0.03424'),
}

VOTING_DATA_R30 = {
    'round': '8th August 2023',
    'total_graviaura_bought_in_$': Decimal('2084.13'), 
    'total_badger_bought_in_$': Decimal('523.34'), 
    'amount_graviaura_bought': Decimal('1270.81'), 
    'amount_badger_bought': Decimal('238.53'), 
    'badger_price_at_the_moment_of_sale_in_$': Decimal('2.194'), 
    'graviaura_price_at_the_moment_of_sale_in_$': Decimal('1.64'), 
    '$/vlAURA for total votes': Decimal('0.00215'), 
    '$/vlAURA without pools': Decimal('0.0297'),
    'llama_vlaura': Decimal('0.03424'),
}

VOTING_ROUNDS = [
    VOTING_DATA_R6, VOTING_DATA_R7, VOTING_DATA_R8, VOTING_DATA_R9, VOTING_DATA_R10,
    VOTING_DATA_R11, VOTING_DATA_R12, VOTING_DATA_R13, VOTING_DATA_R14, VOTING_DATA_R15,
    VOTING_DATA_R16, VOTING_DATA_R17, VOTING_DATA_R18, VOTING_DATA_R19, VOTING_DATA_R20,
    VOTING_DATA_R21, VOTING_DATA_R22, VOTING_DATA_R23, VOTING_DATA_R24, VOTING_DATA_R25,
    VOTING_DATA_R26, VOTING_DATA_R27, VOTING_DATA_R28, VOTING_DATA_R29, VOTING_DATA_R30
]
