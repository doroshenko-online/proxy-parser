class ProxyModel:

    def __init__(self, db_connector, data) -> None:
        self.db_connector = db_connector

        self.ip = data.get('ip')
        self.port = data.get('port')
        self.protocol_id = data.get('protocol_id', '')
        self.created_at = data.get('created_at')
        self.last_check = data.get('last_check')
        self.login = data.get('login')
        self.password = data.get('pass')
        self.resource_id = data.get('from_resource_id', '')
        self.work = data.get('work', False)
        self.google_work = data.get('google_work', False)
        self.country_iso = data.get('country_iso')
        self.last_response_time = data.get('last_response_time')

    async def save(self) -> None:
        """
        Method for update or save new proxy to database
        """
        # TODO: Make saving or update to database
        pass
