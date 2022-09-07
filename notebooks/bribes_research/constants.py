BRIBES_URL = "https://api.llama.airforce/bribes"
DASHBOARD_URL = "https://api.llama.airforce//dashboard"
TABLE_COLUMNS_COMMON_METRICS = [
    "Market", "BADGER bribe", "Total bribe in $", "Fees",
    "Bribes Portion %", "Bribes Portion", "Dilution",
    "$I/O 50%", "$I/O 60%", "$I/O 80%", "$I/O 100%"
]
TABLE_AW_METRIC_HEADERS = [
    "BADGER Bribe", "Total bribe in $", "Average $I/O",
]
PROTOCOL_CVX = "CVX"
PROTOCOL_AURA = "AURA"

BADGER_BRIBE = 42000
STEP = 2000
BADGER_LOW_BOUND = 2000
BADGER_UPPER_BOUND = BADGER_BRIBE
# HH and Votium take 4% on all bribes
FEE = 0.04  # in %

REBALANCING_STEP = 0.00001  # in %

# Order matters here
POOL_WEIGHTS = [0.5, 0.6, 0.8, 1]
