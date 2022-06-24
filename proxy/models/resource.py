class Resource:

    def __init__(self, data) -> None:
        self._id = data.get('id')
        self.name = data.get('name')
        self.addr = data.get('addr')
        self.updated_at = data.get('updated_at')
        self.created_at = data.get('created_at')
