import random
from typing import List
from typing import Tuple

import numpy as np

MINIMAL_FEE = 0.005  # in %
MAX_FEE = 0.05  # in %
# Starting with 1m volume
SIMULATED_VOLUME = 1000000
MIM_LEVERAGES = [1, 2, 3, 4, 5, 6]
LEVERAGE_PROBABILITIES = [50, 40, 30, 20, 10, 1]
DAI_FEES = [0.005, 0.015, 0.03]  # in %
VOLUMES = []

for volume_multiplier in range(1, 16):
    VOLUMES.append(SIMULATED_VOLUME * volume_multiplier)


def _generate_probabilities(
        initial_prob=50, minimal_value=MINIMAL_FEE, max_value=MAX_FEE,
) -> Tuple[List, List]:
    """
    Generates two tables:
    1. Fees values with probability_step_down variable down
    2. Fees probabilities, the lower the fee - the higher probability of fee to appear
    """
    probability_step_down = 4
    possible_fees = []
    probabilities = []
    probability = initial_prob
    for fee in np.arange(minimal_value, max_value, 0.001):
        possible_fees.append(fee)
        probabilities.append(probability)
        if not probability <= probability_step_down:
            probability -= probability_step_down
    return possible_fees, probabilities


def get_tables() -> Tuple[List, List, List, List, List]:
    possible_fees, probabilities = _generate_probabilities()
    revenue_table_minimal_fees = []
    revenue_table_minimal_fees_double = []
    revenue_table_randomized_fees = []
    revenue_table_randomized_fees_double = []

    for sim_volume in VOLUMES:
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
        VOLUMES)


def get_tables_mimlike() -> Tuple[List, List]:
    """
    Simulated fees capture on MIM-like protocol
    """
    fees_capture = 0.3  # in %
    borrow_fee = 0.005  # in %

    revenue_table = []
    for sim_volume in VOLUMES:
        for leverage in MIM_LEVERAGES:
            revenue_table.append(
                [
                    "{:10.4f}".format(sim_volume),
                    f"{fees_capture * 100}%",
                    (sim_volume * leverage) * borrow_fee,
                    f"{borrow_fee * 100}%",
                    leverage
                ])
        revenue_table.append(["-", "-", "-", "-", "-"])
    return revenue_table, VOLUMES


def get_tables_dai_like() -> List:
    revenue_table = []
    for sim_volume in VOLUMES:
        for fee in DAI_FEES:
            revenue_table.append(
                [
                    "{:10.4f}".format(sim_volume),
                    sim_volume * fee,
                    fee,
                ])
        revenue_table.append(["-", "-", "-",])
    return revenue_table
