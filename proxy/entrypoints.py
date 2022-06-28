import asyncio

from proxy.cron.parser import async_cron
from proxy.helpers.db import Db
from proxy.helpers.logger import log
from proxy.models.registry import Registry, DriversEnum


def entrypoint_parser(*args, **kwargs) -> None:
    """
    Entrypoint for parser process
    """
    conf = kwargs['conf']
    # Load registry settings
    Registry.static_path = kwargs.get('static')

    Registry.drivers[DriversEnum.chrome.value] = kwargs['chrome']
    Registry.drivers[DriversEnum.gecko.value] = kwargs['gecko']

    try:
        Registry.driver = Registry.drivers[kwargs['use_driver']]
    except Exception:
        log('Something wrong while setting selenium driver', 'error')
        raise Exception
    
    loop = asyncio.get_event_loop()
    coro = Db._set_db_conector(conf)
    loop.run_until_complete(coro)

    Registry.db_connector = Db.db_connector

    loop.run_until_complete(Registry.load_registry())

    # run async parsers
    asyncio.run(async_cron(conf))