import asyncpg

from proxy.helpers.logger import log

class Db:

    db_connector = None

    def __init__(self, conf) -> None:
        self.database_conf = conf.get('Database')
        if self.database_conf:
            self.host = self.database_conf.get('host')
            self.port = self.database_conf.get('port')
            self.user = self.database_conf.get('user')
            self.password = self.database_conf.get('password')
            self.database = self.database_conf.get('database')
        else:
            log(
                message="Missing config for database",
                level="error"
            )

    async def connect(self):
        log(
            message="Try connect to database",
            level="info"
        )
        conn = await asyncpg.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database
        )
        if not conn:
            log(
                message=f"Can't connect to database {self.database}. Check config and postgres available",
                level="error"
            )
        else:
            log(
                message="Connect to db successfully",
                level="info"
            )
            self.db_connector = conn
            return self.db_connector

    @classmethod
    async def _set_db_conector(cls, conf: dict) -> None:
        if cls.db_connector is None:
            db = cls(conf)
            cls.db_connector = await db.connect()

    @classmethod
    async def get_db_connector(cls, conf: dict = None):
        if cls.db_connector is None and conf:
            connector = await cls._set_db_conector(conf)

        return connector