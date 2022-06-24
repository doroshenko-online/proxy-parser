import asyncpg
from proxy.helpers.logger import log

class Db:


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
            return conn