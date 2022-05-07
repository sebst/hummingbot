from hummingbot.core.api_throttler.data_types import RateLimit

HBOT_ORDER_ID_PREFIX = "latoken-hbot-"
MAX_ORDER_ID_LEN = 36
SNAPSHOT_LIMIT_SIZE = 100
DEFAULT_DOMAIN = "com"
DOMAIN_TO_ENDPOINT = {"com": "api.latoken"}

# Base URL
REST_URL = "https://{}.{}"
WSS_URL = "wss://{}.{}/stomp"

# API versions
PUBLIC_API_VERSION = "/v2"
PRIVATE_API_VERSION = "/v2"

# Public API endpoints or LatokenClient function
# TICKER_PRICE_CHANGE_PATH_URL = "/ticker/24hr"
TICKER_PATH_URL = "/ticker"
CURRENCY_PATH_URL = "/currency"
PAIR_PATH_URL = "/pair"
PING_PATH_URL = "/time"
BOOK_PATH_URL = "/book"
SNAPSHOT_PATH_URL = "/depth"
SERVER_TIME_PATH_URL = "/time"

# Private API endpoints or LatokenClient function
ACCOUNTS_PATH_URL = "/auth/account"
# MY_TRADES_PATH_URL = "/trade"
TRADES_FOR_PAIR_PATH_URL = "/auth/trade/pair"
# ORDER_PATH_URL = "/order"
ORDER_PLACE_PATH_URL = "/auth/order/place"
ORDER_CANCEL_PATH_URL = "/auth/order/cancel"
GET_ORDER_PATH_URL = "/auth/order/getOrder"
USER_ID_PATH_URL = "/auth/user"  # https://api.latoken.com/doc/ws/#section/Accounts
FEES_PATH_URL = "/auth/trade/fee"

WS_HEARTBEAT_TIME_INTERVAL = 30
MAX_ALLOWED_TPS = 100

# Latoken params

SIDE_BUY = 'BUY'
SIDE_SELL = 'SELL'

TIME_IN_FORCE_GTC = 'GTC'  # Good till cancelled
TIME_IN_FORCE_IOC = 'IOC'  # Immediate or cancel
TIME_IN_FORCE_FOK = 'FOK'  # Fill or kill


ACCOUNT = "/auth/account"
TIME = "/time"

# WS (streams)
# Public
BOOK_STREAM = '/v1/book/{symbol}'
TRADES_STREAM = '/v1/trade/{symbol}'
CURRENCIES_STREAM = '/v1/currency'  # All available currencies
PAIRS_STREAM = '/v1/pair'  # All available pairs
TICKER_ALL_STREAM = '/v1/ticker'
TICKERS_PAIR_STREAM = '/v1/ticker/{base}/{quote}'  # 24h and 7d volume and change + last price for pairs
RATES_STREAM = '/v1/rate/{base}/{quote}'
RATES_QUOTE_STREAM = '/v1/rate/{quote}'

# Private
ORDERS_STREAM = '/user/{user}/v1/order'
ACCOUNTS_STREAM = '/user/{user}/v1/account/total'  # Returns all accounts of a user including empty ones
ACCOUNT_STREAM = '/user/{user}/v1/account'
TRANSACTIONS_STREAM = '/user/{user}/v1/transaction'  # Returns external transactions (deposits and withdrawals)
TRANSFERS_STREAM = '/user/{user}/v1/transfers'  # Returns internal transfers on the platform (inter_user, ...)

# Rate Limit time intervals
ONE_MINUTE = 60
ONE_SECOND = 1
ONE_DAY = 86400

MAX_REQUEST = 5000

SUBSCRIPTION_ID_ACCOUNT = 0
SUBSCRIPTION_ID_BOOKS = 1
SUBSCRIPTION_ID_TRADES = 2
SUBSCRIPTION_ID_ORDERS = 3
# # Websocket event types
DIFF_EVENT_TYPE = "depthUpdate"
TRADE_EVENT_TYPE = "trade"

GLOBAL_RATE_LIMIT = "global"

# Rate Limit Type
# REQUEST_WEIGHT = "REQUEST_WEIGHT"
# ORDERS = "ORDERS"
# ORDERS_24HR = "ORDERS_24HR"
RATE_LIMITS = [
    RateLimit(limit_id=GLOBAL_RATE_LIMIT, limit=MAX_ALLOWED_TPS, time_interval=ONE_SECOND),
]
