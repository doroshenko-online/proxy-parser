from asyncpg import Connection
from typing import List, TypeVar

from proxy.helpers.logger import log

SelfProtocol = TypeVar("SelfProtocol", bound="ProtocolModel")


class ProtocolModel:

    def __init__(self, data: dict) -> None:
        self._id = data.get('id')
        self.ptype = data.get('protocol_name')

    @property
    def type(self) -> str:
        return self.ptype

    @property
    def id(self) -> str:
        return self._id

    @staticmethod
    async def get_protocol_by_type(protocol_type: str) -> SelfProtocol:
        '''
        Get protocol object by type
        @param protocol_type: protocol name
        @return: Protocol object
        '''
        # TODO: Make load protocol from database
        pass
    
    @classmethod
    async def get_protocols(cls, db_connector: Connection) -> List[SelfProtocol]:
        stmt = await db_connector.prepare("SELECT id, protocol_name FROM protocols")
        log('Getting protocols', 'info')

        async with db_connector.transaction():

            return [cls(proto) async for proto in stmt.cursor()]
