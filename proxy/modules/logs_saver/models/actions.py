from asyncpg import Connection
from typing import List, TypeVar

from proxy.helpers.logger import log

SelfBaseAction = TypeVar("SelfBaseAction", bound="BaseAction")


class BaseAction:

    def __init__(self, data) -> None:
        self._id = data.get('id')
        self.name = data.get('action_name')

    @classmethod
    async def get_actions(cls, db_connector: Connection) -> List[SelfBaseAction]:
        stmt = await db_connector.prepare("SELECT * FROM actions")
        log('Getting actions')

        async with db_connector.transaction():
            return [cls(resource) async for resource in stmt.cursor()]