from random import uniform
from typing import List
from typing import Tuple

MINIMAL_FEE = 0.005  # in %
MAX_FEE = 0.05  # in %
# Starting with 10m volume
SIMULATED_VOLUME = 1000000


def get_tables() -> Tuple[List, List]:
    volumes = []
    for volume_multiplier in range(1, 16):
        volumes.append(SIMULATED_VOLUME * volume_multiplier)
    revenue_table_minimal_fees = []
    revenue_table_randomized_fees = []
    for sim_volume in volumes:
        revenue_table_minimal_fees.append(
            ["{:10.4f}".format(sim_volume), sim_volume * MINIMAL_FEE, MINIMAL_FEE * 100])
        random_fee = uniform(float(MINIMAL_FEE), float(MAX_FEE))
        revenue_table_randomized_fees.append(
            ["{:10.4f}".format(sim_volume), sim_volume * random_fee, random_fee * 100])
    return revenue_table_minimal_fees, revenue_table_randomized_fees
