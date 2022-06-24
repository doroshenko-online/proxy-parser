from pyparsing import Optional
from typing import Optional

from proxy.models.protocol import Protocol
from proxy.models.resource import Resource


class Registry:

    protocols = {}
    resources = {}
    user_roles = {}
    actions = {}

    @classmethod
    def get_protocol(cls, protocol_id: str) -> Optional[Protocol]:
        # TODO: get protocol by id from registry

        if protocol_id:
            pass
        else:
            return None

    @classmethod
    def get_resource(cls, recource_id: str) -> Optional[Resource]:
        # TODO: get recource by id from registry

        if recource_id:
            pass
        else:
            return None

    @classmethod
    def get_user_role(cls, role_id: str) -> Optional[UserRole]:
        # TODO: get user_role by id from registry
        if role_id:
            pass
        else:
            return None

    @classmethod
    def get_action(cls, action_id: str) -> Optional[Action]:
        # TODO: get action by id from registry
        if action_id:
            pass
        else:
            return None

    @classmethod
    async def load_registry(cls) -> None:
        """
        Load registry info
        """
        # TODO: load protocols
        # TODO: load resources
        # TODO: load user_roles
        # TODO: load actions
        print('Registry loaded')
