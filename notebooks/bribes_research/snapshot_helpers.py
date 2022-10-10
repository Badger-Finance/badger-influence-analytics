import logging
import re
from dataclasses import dataclass
from typing import Dict
from typing import Optional

from gql import Client
from gql import gql
from gql.transport.requests import RequestsHTTPTransport
from gql.transport.requests import log

log.setLevel(logging.WARNING)

SNAPSHOT_STATE_ACTIVE = "active"
SNAPSHOT_STATE_CLOSED = "closed"
SNAPSHOT_MIN_AMOUNT_POOLS = 10
SNAPSHOT_GQL_API_URL = "https://hub.snapshot.org/graphql"


GET_PROPOSALS_Q = lambda first, skip, space: gql(f"""
query {{
  proposals (
    first: {first},
    skip: {skip},
    where: {{
      space_in: ["{space}"],
      network_in: ["1"]
    }},
    orderBy: "created",
    orderDirection: desc
  ) {{
    id
    title
    choices
    start
    end
    snapshot
    network
    state
  }}
}}
""")


@dataclass
class Snapshots:
    current_snapshot: Optional[Dict] = None
    previous_snapshot: Optional[Dict] = None


def make_gql_client(url: str) -> Optional[Client]:
    transport = RequestsHTTPTransport(url=url, retries=3)
    return Client(
        transport=transport, fetch_schema_from_transport=True, execute_timeout=60
    )


def get_active_and_previous_snapshots() -> Optional[Snapshots]:
    """

    """
    snapshots = Snapshots()
    client = make_gql_client(SNAPSHOT_GQL_API_URL)
    limit = 100
    offset = 0
    while True:
        result = client.execute(GET_PROPOSALS_Q(
            first=limit, skip=offset, space="aurafinance.eth")
        )
        offset += limit
        if not result or not result.get("proposals"):
            break
        for proposal in result['proposals']:
            match = re.match(r"Gauge Weight for Week of .+", proposal['title'])
            number_of_choices = len(proposal['choices'])
            if (
                    match and number_of_choices > SNAPSHOT_MIN_AMOUNT_POOLS
                    and proposal['state'] == SNAPSHOT_STATE_ACTIVE
            ):
                snapshots.current_snapshot = proposal
            elif (
                    match and number_of_choices > SNAPSHOT_MIN_AMOUNT_POOLS
                    and proposal['state'] == SNAPSHOT_STATE_CLOSED
            ):
                snapshots.previous_snapshot = proposal
            # Once previous snapshot is found - break loop and return
            if snapshots.previous_snapshot:
                break
        return snapshots
