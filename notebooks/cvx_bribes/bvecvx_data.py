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
    '$/vlCVX without badgerwbtc': Decimal('0.066'),
    'llama_vlcvx': Decimal('0.06832'),
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
    '$/vlCVX without badgerwbtc': Decimal('0.088'),
    'llama_vlcvx': Decimal('0.09030'),
}

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
    '$/vlCVX without badgerwbtc': Decimal('0.0643'),
    'llama_vlcvx': Decimal('0.06436'),
}

BRIBES_HARVESTED_DATA_R25 = {"2pool-frax": Decimal(79413.61100609367262977928944),
                             "frax": Decimal(133831.2485283798421340128355),
                             "fpifrax": Decimal(606275.2833809552228298586112),
                             "tusd": Decimal(541963.5299455261134157644223),
                             "alusd": Decimal(430654.7259226680394298321723),
                             "aleth": Decimal(450442.9577489539192495534612),
                             "f-badgerwbtc": Decimal(230947.6217531580304679192000)}

VOTING_DATA_R26 = {
    'round': "1st Sep 2022t",
    'total_cvx_sold_in_$': Decimal('106407.872'),
    'total_badger_sold_in_$': Decimal('40399.96'),
    'amount_cvx': Decimal('19668.74'),
    'amount_badger': Decimal('9266.045'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('4.36'),
    'cvx_price_at_the_moment_of_sale_in_$': Decimal('5.41'),
    '$/vlCVX for total votes': Decimal('0.058'),
    '$/vlCVX without badgerwbtc': Decimal('0.064'),
    'llama_vlcvx': Decimal('0.06215'),
}

BRIBES_HARVESTED_DATA_R26 = {"FRAX+USDC (0xDcEF...41A2)": Decimal(14975.95741255921645546083958),
                             "FRAX+3Crv (0xd632...Ed3B)": Decimal(14975.95741255921645546083958),
                             "FRAX+FPI (0xf861...d37c)": Decimal(427342.0623236903590017640403),
                             "USDC+EURS (0x98a7...eB8B)": Decimal(636070.5845626579743647076321),
                             "alUSD+3Crv (0x43b4...3f8c)": Decimal(602979.4773784314011974116968),
                             "ETH+alETH (0xC4C3...784e)": Decimal(608070.4169452354893769956868),
                             "BADGER+WBTC (0x50f3...685d)": Decimal(241055.3273669102916382362500)}

VOTING_DATA_R27 = {
    'round': "15th September",
    'total_cvx_sold_in_$': Decimal('86649.570'),
    'total_badger_sold_in_$': Decimal('32621.784'),
    'amount_cvx': Decimal('18334.653'),
    'amount_badger': Decimal('8279.641'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('3.94'),
    'cvx_price_at_the_moment_of_sale_in_$': Decimal('4.726'),
    '$/vlCVX for total votes': Decimal('0.047'),
    '$/vlCVX without badgerwbtc': Decimal('0.052'),
    'llama_vlcvx': Decimal('0.059'),
}

BRIBES_HARVESTED_DATA_R27 = {"FRAX+3Crv": 523768.0775055959188242345514,
                             "FRAX+USDC": 147193.6139976382742690570023,
                             "FRAX+FPI": 70860.95247575496794030479476,
                             "USDD+3Crv": 437257.7277807948383183153855,
                             "TUSD+3Crv": 488146.1687953837092041501890,
                             "ApeUSD+crvFRAX": 635722.6477376914347730711191,
                             "BADGER+WBTC": 241472.8624365842597188099500}

VOTING_DATA_R28 = {
    'round': "29th Sep 2022",
    'total_cvx_sold_in_$': Decimal('106512.74'),
    'total_badger_sold_in_$': Decimal('40568.72'),
    'amount_cvx': Decimal('20483.22'),
    'amount_badger': Decimal('11145.25'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('3.64'),
    'cvx_price_at_the_moment_of_sale_in_$': Decimal('5.2'),
    '$/vlCVX for total votes': Decimal('0.058'),
    '$/vlCVX without badgerwbtc': Decimal('0.064'),
    'llama_vlcvx': Decimal('0.05939'),
}

VOTING_DATA_R29 = {
    'round': "13th Oct 2022",
    'total_cvx_sold_in_$': Decimal('83810.609'),
    'total_badger_sold_in_$': Decimal('31898.119'),
    'amount_cvx': Decimal('15855.204'),
    'amount_badger': Decimal('9409.48'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('3.39'),
    'cvx_price_at_the_moment_of_sale_in_$': Decimal('5.29'),
    '$/vlCVX for total votes': Decimal('0.0455'),
    '$/vlCVX without badgerwbtc': Decimal('0.050'),
    'llama_vlcvx': Decimal('0.04901'),
}

VOTING_DATA_R30 = {
    'round': "27th Oct 2022",
    'total_cvx_sold_in_$': Decimal('93843.92'),
    'total_badger_sold_in_$': Decimal('35508.54'),
    'amount_cvx': Decimal('18050.38'),
    'amount_badger': Decimal('10474.50'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('3.39'),
    'cvx_price_at_the_moment_of_sale_in_$': Decimal('5.2'),
    '$/vlCVX for total votes': Decimal('0.051'),
    '$/vlCVX without badgerwbtc': Decimal('0.057'),
    'llama_vlcvx': Decimal('0.055'),
}

VOTING_DATA_R31 = {
    'round': "10th Nov 2022",
    'total_cvx_sold_in_$': Decimal('54464.38'),
    'total_badger_sold_in_$': Decimal('20774.91'),
    'amount_cvx': Decimal('13238.79'),
    'amount_badger': Decimal('8179.1'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('2.54'),
    'cvx_price_at_the_moment_of_sale_in_$': Decimal('4.114'),
    '$/vlCVX for total votes': Decimal('0.04'),
    '$/vlCVX without badgerwbtc': Decimal('0.0444'),
    'llama_vlcvx': Decimal('0.041'),
}

VOTING_DATA_R32 = {
    'round': "24th Nov 2022",
    'total_cvx_sold_in_$': Decimal('45019.8'),
    'total_badger_sold_in_$': Decimal('17119.7'),
    'amount_cvx': Decimal('11345.71'),
    'amount_badger': Decimal('6609.82'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('2.59'),
    'cvx_price_at_the_moment_of_sale_in_$': Decimal('3.97'),
    '$/vlCVX for total votes': Decimal('0.036'),
    '$/vlCVX without badgerwbtc': Decimal('0.0413'),
    'llama_vlcvx': Decimal('0.03976'),
}

VOTING_DATA_R33 = {
    'round': "8th Dec 2022",
    'total_cvx_sold_in_$': Decimal('46306.37'),
    'total_badger_sold_in_$': Decimal('17576.08'),
    'amount_cvx': Decimal('11661.14'),
    'amount_badger': Decimal('6812.44'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('2.6'),
    'cvx_price_at_the_moment_of_sale_in_$': Decimal('3.97'),
    '$/vlCVX for total votes': Decimal('0.037'),
    '$/vlCVX without badgerwbtc': Decimal('0.0424'),
    'llama_vlcvx': Decimal('0.03958'),
}

VOTING_DATA_R34 = {
    'round': '22th Dec 2022',
    'total_cvx_sold_in_$': Decimal('34296.3'),
    'total_badger_sold_in_$': Decimal('13004.2'),
    'amount_cvx': Decimal('10727.6'),
    'amount_badger': Decimal('6134.03'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('2.12'),
    'cvx_price_at_the_moment_of_sale_in_$': Decimal('3.2'),
    '$/vlCVX for total votes': Decimal('0.0292'),
    '$/vlCVX without badgerwbtc': Decimal('0.031'),
    'llama_vlcvx': Decimal('0.032'),
}

VOTING_DATA_R35 = {
    'round': '5th Jan 2023',
    'total_cvx_sold_in_$': Decimal('45313.07'),
    'total_badger_sold_in_$': Decimal('17053.60'),
    'amount_cvx': Decimal('13474.001'),
    'amount_badger': Decimal('7319.142'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('2.33'),
    'cvx_price_at_the_moment_of_sale_in_$': Decimal('3.4'),
    '$/vlCVX for total votes': Decimal('0.0379'),
    '$/vlCVX without badgerwbtc': Decimal('0.040'),
    'llama_vlcvx': Decimal('0.03932'),
}

VOTING_DATA_R36 = {
    'round': '19th Jan 2023',
    'total_cvx_sold_in_$': Decimal('63997.40'),
    'total_badger_sold_in_$': Decimal('24377.10'),
    'amount_cvx': Decimal('12155.25'),
    'amount_badger': Decimal('8319.84'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('2.93'),
    'cvx_price_at_the_moment_of_sale_in_$': Decimal('5.27'),
    '$/vlCVX for total votes': Decimal('0.053'),
    '$/vlCVX without badgerwbtc': Decimal('0.056'),
    'llama_vlcvx': Decimal('0.05192'),
}

VOTING_DATA_R37 = {
    'round': '2nd Feb 2023',
    'total_cvx_sold_in_$': Decimal('86607.064'),
    'total_badger_sold_in_$': Decimal('32472.64'),
    'amount_cvx': Decimal('13279.22'),
    'amount_badger': Decimal('10179.51'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('3.19'),
    'cvx_price_at_the_moment_of_sale_in_$': Decimal('6.522'),
    '$/vlCVX for total votes': Decimal('0.0653'),
    '$/vlCVX without badgerwbtc': Decimal('0.0687'),
    'llama_vlcvx': Decimal('0.06227'),
}

VOTING_DATA_R38 = {
    'round': '16th Feb 2023',
    'total_cvx_sold_in_$': Decimal('76085.11'),
    'total_badger_sold_in_$': Decimal('28574.99'),
    'amount_cvx': Decimal('12052.13'),
    'amount_badger': Decimal('8297.04'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('3.444'),
    'cvx_price_at_the_moment_of_sale_in_$': Decimal('6.31'),
    '$/vlCVX for total votes': Decimal('0.059'),
    '$/vlCVX without badgerwbtc': Decimal('0.063'),
    'llama_vlcvx': Decimal('0.06293'),
}

VOTING_DATA_R39 = {
    'round': '2nd Mar 2023',
    'total_cvx_sold_in_$': Decimal('44150.003'),
    'total_badger_sold_in_$': Decimal('16673.07'),
    'amount_cvx': Decimal('7430.16'),
    'amount_badger': Decimal('5446.94'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('3.06'),
    'cvx_price_at_the_moment_of_sale_in_$': Decimal('5.94'),
    '$/vlCVX for total votes': Decimal('0.054'),
    '$/vlCVX without badgerwbtc': Decimal('0.059'),
    'llama_vlcvx': Decimal('0.05061'),
}

VOTING_DATA_R40 = {
    'round': '16th Mar 2023',
    'total_cvx_sold_in_$': Decimal('49276.94'),
    'total_badger_sold_in_$': Decimal('18647.212'),
    'amount_cvx': Decimal('9020.123'),
    'amount_badger': Decimal('5901.02'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('3.16'),
    'cvx_price_at_the_moment_of_sale_in_$': Decimal('5.463'),
    '$/vlCVX for total votes': Decimal('0.044'),
    '$/vlCVX without badgerwbtc': Decimal('0.0462'),
    'llama_vlcvx': Decimal('0.04345'),
}

VOTING_DATA_R41 = {
    'round': '30th Mar 2023',
    'total_cvx_sold_in_$': Decimal('56042.71'),
    'total_badger_sold_in_$': Decimal('21073.87'),
    'amount_cvx': Decimal('10590.1'),
    'amount_badger': Decimal('7613.4'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('2.77'),
    'cvx_price_at_the_moment_of_sale_in_$': Decimal('5.3'),
    '$/vlCVX for total votes': Decimal('0.0494'),
    '$/vlCVX without badgerwbtc': Decimal('0.0534'),
    'llama_vlcvx': Decimal('0.04874'),
}

VOTING_DATA_R42 = {
    'round': '13th Apr 2023',
    'total_cvx_sold_in_$': Decimal('76387.9'),
    'total_badger_sold_in_$': Decimal('29379.8'),
    'amount_cvx': Decimal('12418.8'),
    'amount_badger': Decimal('9350.7'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('3.14'),
    'cvx_price_at_the_moment_of_sale_in_$': Decimal('6.15'),
    '$/vlCVX for total votes': Decimal('0.057'),
    '$/vlCVX without badgerwbtc': Decimal('0.0622'),
    'llama_vlcvx': Decimal('0.05899'),
}

VOTING_DATA_R43 = {
    'round': '27th Apr 2023',
    'total_cvx_sold_in_$': Decimal('59040.3'),
    'total_badger_sold_in_$': Decimal('22551.23'),
    'amount_cvx': Decimal('11592.44'),
    'amount_badger': Decimal('8097.4'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('2.79'),
    'cvx_price_at_the_moment_of_sale_in_$': Decimal('5.1'),
    '$/vlCVX for total votes': Decimal('0.043'),
    '$/vlCVX without badgerwbtc': Decimal('0.0472'),
    'llama_vlcvx': Decimal('0.04482'),
}

VOTING_DATA_R44 = {
    'round': '11th May 2023',
    'total_cvx_sold_in_$': Decimal('63975.6'),
    'total_badger_sold_in_$': Decimal('24296.24'),
    'amount_cvx': Decimal('13603.14'),
    'amount_badger': Decimal('9546.66'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('2.54'),
    'cvx_price_at_the_moment_of_sale_in_$': Decimal('4.7'),
    '$/vlCVX for total votes': Decimal('0.042'),
    '$/vlCVX without badgerwbtc': Decimal('0.046'),
    'llama_vlcvx': Decimal('0.04321'),
}

VOTING_DATA_R45 = {
    'round': '25th May 2023',
    'total_cvx_sold_in_$': Decimal('60632.46'),
    'total_badger_sold_in_$': Decimal('23001.17'),
    'amount_cvx': Decimal('13833.55'),
    'amount_badger': Decimal('9263.46'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('2.48'),
    'cvx_price_at_the_moment_of_sale_in_$': Decimal('4.38'),
    '$/vlCVX for total votes': Decimal('0.04'),
    '$/vlCVX without badgerwbtc': Decimal('0.041'),
    'llama_vlcvx': Decimal('0.0434'),
}

VOTING_DATA_R46 = {
    'round': '8th Jun 2023',
    'total_cvx_sold_in_$': Decimal('53806.69'),
    'total_badger_sold_in_$': Decimal('20276.55'),
    'amount_cvx': Decimal('15755.98'),
    'amount_badger': Decimal('10072.8'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('2.013'),
    'cvx_price_at_the_moment_of_sale_in_$': Decimal('3.42'),
    '$/vlCVX for total votes': Decimal('0.034'),
    '$/vlCVX without badgerwbtc': Decimal('0.0363'),
    'llama_vlcvx': Decimal('0.035'),
}

VOTING_DATA_R47 = {
    'round': '22nd Jun 2023',
    'total_cvx_sold_in_$': Decimal('52709.14'), 
    'total_badger_sold_in_$': Decimal('19844.61'), 
    'amount_cvx': Decimal('14999.76'), 
    'amount_badger': Decimal('9016.18'), 
    'badger_price_at_the_moment_of_sale_in_$': Decimal('2.20'), 
    'cvx_price_at_the_moment_of_sale_in_$': Decimal('3.51'), 
    '$/vlCVX for total votes': Decimal('0.034'), 
    '$/vlCVX without badgerwbtc': Decimal('0.037'),
    'llama_vlcvx': Decimal('0.03696'),
}

VOTING_DATA_R48 = {
    'round': '11th Jul 2023',
    'total_cvx_sold_in_$': Decimal('41555.35'), 
    'total_badger_sold_in_$': Decimal('15691.78'), 
    'amount_cvx': Decimal('10319.18'), 
    'amount_badger': Decimal('7380.89'), 
    'badger_price_at_the_moment_of_sale_in_$': Decimal('2.126'), 
    'cvx_price_at_the_moment_of_sale_in_$': Decimal('4.027'), 
    '$/vlCVX for total votes': Decimal('0.0367'), 
    '$/vlCVX without badgerwbtc': Decimal('0.0399'),
    'llama_vlcvx': Decimal('0.03659'),
}

VOTING_DATA_R49 = {
    'round': '25th Jul 2023',
    'total_cvx_sold_in_$': Decimal('23369.26'), 
    'total_badger_sold_in_$': Decimal('8829.62'), 
    'amount_cvx': Decimal('6779.59'), 
    'amount_badger': Decimal('4232.80'),
    'badger_price_at_the_moment_of_sale_in_$': Decimal('2.086'), 
    'cvx_price_at_the_moment_of_sale_in_$': Decimal('3.447'), 
    '$/vlCVX for total votes': Decimal('0.0346'), 
    '$/vlCVX without badgerwbtc': Decimal('0.0387'),
    'llama_vlcvx': Decimal('0.03746'),
}

VOTING_DATA_R50 = {
    'round': '8th Aug 2023',
    'total_cvx_sold_in_$': Decimal('17364.25'), 
    'total_badger_sold_in_$': Decimal('6572.99'), 
    'amount_cvx': Decimal('5339.56'), 
    'amount_badger': Decimal('2998.63'), 
    'badger_price_at_the_moment_of_sale_in_$': Decimal('2.192'), 
    'cvx_price_at_the_moment_of_sale_in_$': Decimal('3.252'), 
    '$/vlCVX for total votes': Decimal('0.027'), 
    '$/vlCVX without badgerwbtc': Decimal('0.0302'),
    'llama_vlcvx': Decimal('0.03026'),
}

VOTING_DATA_R51 = {
    'round': '22nd Aug 2023',
    'total_cvx_sold_in_$': Decimal('9747.63'), 
    'total_badger_sold_in_$': Decimal('3671.29'), 
    'amount_cvx': Decimal('3459.058'), 
    'amount_badger': Decimal('1833.81'), 
    'badger_price_at_the_moment_of_sale_in_$': Decimal('2.002'), 
    'cvx_price_at_the_moment_of_sale_in_$': Decimal('2.818'), 
    '$/vlCVX for total votes': Decimal('0.0223'), 
    '$/vlCVX without badgerwbtc': Decimal('0.02565'),
    'llama_vlcvx': Decimal('0.02513'),
}

VOTING_DATA_R52 = {
    'round': '5th Sep 2023',
    'total_cvx_sold_in_$': Decimal('9546.72'), 
    'total_badger_sold_in_$': Decimal('3604.93'), 
    'amount_cvx': Decimal('3603.90'), 
    'amount_badger': Decimal('1755.93'), 
    'badger_price_at_the_moment_of_sale_in_$': Decimal('2.053'), 
    'cvx_price_at_the_moment_of_sale_in_$': Decimal('2.65'), 
    '$/vlCVX for total votes': Decimal('0.0237'), 
    '$/vlCVX without badgerwbtc': Decimal('0.0277'),
    'llama_vlcvx': Decimal('0.02710'),
}

VOTING_DATASETS = [
    VOTING_DATA_R23, VOTING_DATA_R24, VOTING_DATA_R25, VOTING_DATA_R26, VOTING_DATA_R27,
    VOTING_DATA_R28, VOTING_DATA_R29, VOTING_DATA_R30, VOTING_DATA_R31, VOTING_DATA_R32,
    VOTING_DATA_R33, VOTING_DATA_R34, VOTING_DATA_R35, VOTING_DATA_R36, VOTING_DATA_R37,
    VOTING_DATA_R38, VOTING_DATA_R39, VOTING_DATA_R40, VOTING_DATA_R41, VOTING_DATA_R42,
    VOTING_DATA_R43, VOTING_DATA_R44, VOTING_DATA_R45, VOTING_DATA_R46, VOTING_DATA_R47,
    VOTING_DATA_R48, VOTING_DATA_R49, VOTING_DATA_R50, VOTING_DATA_R51, VOTING_DATA_R52,
]
