from proxy.models.users.base_user import BaseUser


class User(BaseUser):

    def __init__(self, data) -> None:
        super(User, data)
