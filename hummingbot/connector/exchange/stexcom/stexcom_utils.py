from typing import Any, Dict

from hummingbot.client.config.config_methods import using_exchange
from hummingbot.client.config.config_var import ConfigVar

CENTRALIZED = True
EXAMPLE_PAIR = "LA-USDT"
DEFAULT_FEES = [0.1, 0.1]

# def is_pair_valid(pair_data: Dict[str, Any]) -> bool:
#     return pair_data["status"] == 'PAIR_STATUS_ACTIVE'


def is_exchange_information_valid(pair_data: Dict[str, Any]) -> bool:
    """
    Verifies if a trading pair is enabled to operate with based on its exchange information
    :param pair_data: the exchange information for a trading pair
    :return: True if the trading pair is enabled, False otherwise
    """
    # pair_details = pair_data["id"]
    pair_base = pair_data["baseCurrency"]
    pair_quote = pair_data["quoteCurrency"]

    return pair_data["is_valid"] and pair_data["status"] == 'PAIR_STATUS_ACTIVE' and \
        isinstance(pair_base, dict) and isinstance(pair_quote, dict) and \
        pair_base["status"] == 'CURRENCY_STATUS_ACTIVE' and pair_base["type"] == 'CURRENCY_TYPE_CRYPTO' and \
        pair_quote["status"] == 'CURRENCY_STATUS_ACTIVE' and pair_quote["type"] == 'CURRENCY_TYPE_CRYPTO'


KEYS = {
    "latoken_api_key":
        ConfigVar(key="latoken_api_key",
                  prompt="Enter your Latoken API key >>> ",
                  required_if=using_exchange("latoken"),
                  is_secure=True,
                  is_connect_key=True),
    "latoken_api_secret":
        ConfigVar(key="latoken_api_secret",
                  prompt="Enter your Latoken API secret >>> ",
                  required_if=using_exchange("latoken"),
                  is_secure=True,
                  is_connect_key=True),
}


OTHER_DOMAINS = []
OTHER_DOMAINS_PARAMETER = {}
OTHER_DOMAINS_EXAMPLE_PAIR = {}
OTHER_DOMAINS_DEFAULT_FEES = {}
OTHER_DOMAINS_KEYS = {}
