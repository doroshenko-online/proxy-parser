class Protocol:

    def __init__(self, data: dict) -> None:
        self._id = data.get('id')
        self.type = data.get('protocol_name')

    @property
    def type(self) -> str:
        return self.type

    @property
    def id(self) -> str:
        return self._id

    @staticmethod
    async def get_protocol_by_type(protocol_type: str) -> Protocol:
        '''
        Get protocol object by type
        @param protocol_type: protocol name
        @return: Protocol object
        '''
        # TODO: Make load protocol from database
        pass
