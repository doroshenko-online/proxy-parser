from proxy.models.registry import Registry

class BaseUser:

    def __init__(self, data) -> None:
        self._id = data.get('_id')
        self.username = data.get('username')
        self.password = data.get('password')
        self.role = Registry.get_user_role(data.get('role'))
        self.created_at = data.get('created_at')
        self.country_iso = data.get('country_iso')
        self.ip = data.get('ip')

    async def save(self) -> None:
        pass
