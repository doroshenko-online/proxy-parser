from enum import Enum
from typing import Optional

from proxy.helpers.logger import log
from proxy.models.protocol import ProtocolModel
from proxy.models.resource import ResourceModel
from proxy.models.users.user_role import UserRole

from proxy.modules.logs_saver.models.actions import BaseAction


class DriversEnum(Enum):
    off = 0
    chrome = 1
    gecko = 2


class Registry:

    protocols = {}
    resources = {}
    user_roles = {}
    actions = {}
    static_path = None
    drivers = {DriversEnum.off.value: None}
    driver = None
    db_connector = None

    @classmethod
    def get_protocol(cls, protocol_id: int) -> Optional[ProtocolModel]:
        return cls.protocols.get(protocol_id)

    @classmethod
    def get_resource(cls, recource_id: int) -> Optional[ResourceModel]:
        return cls.resources.get(recource_id)

    @classmethod
    def get_user_role(cls, role_id: int) -> Optional[UserRole]:
        return cls.user_roles.get(role_id)

    @classmethod
    async def load_registry(cls) -> None:
        """
        Load registry info
        """
        await cls._load_protocols()
        await cls._load_resources()
        await cls._load_user_roles()
        await cls._load_actions()
        log('Registry loaded', 'info')

    @classmethod
    async def _load_protocols(cls) -> None:
        for proto in await ProtocolModel.get_protocols(cls.db_connector):
            cls.protocols[proto._id] = proto
    @classmethod
    async def _load_resources(cls) -> None:
        for res in await ResourceModel.get_resources(cls.db_connector):
            cls.resources[res._id] = res

    @classmethod
    async def _load_user_roles(cls) -> None:
        for role in await UserRole.get_roles(cls.db_connector):
            cls.user_roles[role._id] = role

    @classmethod
    async def _load_actions(cls) -> None:
        for action in await BaseAction.get_actions(cls.db_connector):
            cls.actions[action._id] = action
