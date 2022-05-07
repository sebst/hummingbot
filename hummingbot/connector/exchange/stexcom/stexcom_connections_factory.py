from hummingbot.connector.exchange.stexcom.stexcom_ws_connection import StexcomWSConnection
from hummingbot.core.web_assistant.connections.connections_factory import ConnectionsFactory


class StexcomConnectionsFactory(ConnectionsFactory):

    async def get_ws_connection(self) -> StexcomWSConnection:
        shared_client = await self._get_shared_client()
        connection = StexcomWSConnection(aiohttp_client_session=shared_client)
        return connection
