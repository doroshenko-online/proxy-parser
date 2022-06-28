from asyncpg import Connection
from typing import List, TypeVar

from proxy.enums import ParserHandlersEnum
from proxy.helpers.logger import log

SelfResource = TypeVar("SelfResource", bound="ResourceModel")


class ResourceModel:

    def __init__(self, data) -> None:
        self._id = data.get('id')
        self.name = data.get('name')
        self.addr = data.get('addr')
        self.updated_at = data.get('updated_at')
        self.created_at = data.get('created_at')
        self.handler = (getattr(ParserHandlersEnum, self.name).value)()
        self.handler.model = self

    @classmethod
    async def get_resources(cls, db_connector: Connection) -> List[SelfResource]:
        stmt = await db_connector.prepare("SELECT * FROM resources")
        log('Getting resources', 'info')

        async with db_connector.transaction():
            return [cls(resource) async for resource in stmt.cursor()]
