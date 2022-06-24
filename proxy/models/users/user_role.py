from asyncpg import Connection
from enum import Enum
from typing import List, TypeVar

from proxy.helpers.logger import log

SelfRole = TypeVar("SelfRole", bound="UserRole")


class UserRolesEnum(Enum):
    superadmin = 0
    admin = 1
    api_user = 2
    web_user = 3
    guest = 0


class UserRole:

    def __init__(self, data) -> None:
        self._id = data.get('id')
        self.name = data.get('name')
        self.priority = data.get('priority', UserRolesEnum.guest.value)

    @classmethod
    async def get_roles(cls, db_connector: Connection) -> List[SelfRole]:
        stmt = await db_connector.prepare("SELECT * FROM user_roles")
        log('Getting user roles')

        async with db_connector.transaction():
            return [cls(resource) async for resource in stmt.cursor()]