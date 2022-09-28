import random
from typing import List
from typing import Tuple

import numpy as np

MINIMAL_FEE = 0.005  # in %
MAX_FEE = 0.05  # in %
# Starting with 10m volume
SIMULATED_VOLUME = 1000000


def _generate_probabilities() -> Tuple[List, List]:
    """
    Generates two tables:
    1. Fees values with probability_step_down variable down
    2. Fees probabilities, the lower the fee - the higher probability of fee to appear
    """
    initial_probability = 50
    probability_step_down = 4
    possible_fees = []
    probabilities = []
    probability = initial_probability
    for fee in np.arange(MINIMAL_FEE, MAX_FEE, 0.001):
        possible_fees.append(fee)
        probabilities.append(probability)
        if not probability <= probability_step_down:
            probability -= probability_step_down
    return possible_fees, probabilities


def get_tables() -> Tuple[List, List, List, List, List]:
    possible_fees, probabilities = _generate_probabilities()
    volumes = []
    for volume_multiplier in range(1, 16):
        volumes.append(SIMULATED_VOLUME * volume_multiplier)
    revenue_table_minimal_fees = []
    revenue_table_minimal_fees_double = []
    revenue_table_randomized_fees = []
    revenue_table_randomized_fees_double = []

    for sim_volume in volumes:
        revenue_table_minimal_fees.append(
            ["{:10.4f}".format(sim_volume), sim_volume * MINIMAL_FEE, f"{MINIMAL_FEE * 100}%"])
        revenue_table_minimal_fees_double.append(
            ["{:10.4f}".format(sim_volume),
             sim_volume * (MINIMAL_FEE * 2),
             f"{(MINIMAL_FEE * 2) * 100}%"]
        )
        random_fee = random.choices(possible_fees, probabilities)[0]
        revenue_table_randomized_fees.append(
            ["{:10.4f}".format(sim_volume), sim_volume * random_fee, f"{random_fee * 100}%"])
        revenue_table_randomized_fees_double.append(
            ["{:10.4f}".format(sim_volume), sim_volume * (random_fee * 2),
             f"{(random_fee * 2) * 100}%"]
        )
    return (
        revenue_table_minimal_fees,
        revenue_table_minimal_fees_double,
        revenue_table_randomized_fees,
        revenue_table_randomized_fees_double,
        volumes)
