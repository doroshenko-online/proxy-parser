import asyncio
import datetime

from proxy.helpers.logger import log
from proxy.models.registry import Registry
from proxy.utils import get_timeout_from_config_value


async def async_cron(conf: dict) -> None:

    while True:
        parse_timeout = get_timeout_from_config_value(conf['App']['proxy_parse_timeout'])
        tasks = [resource.handler.run() for resource in Registry.resources.values()]

        start_parse = datetime.datetime.now()
        log('Start parsing...')
        await asyncio.gather(*tasks)
        parser_work_second = datetime.datetime.now() - start_parse
        log(f'Parsing done for {parser_work_second.seconds} seconds. Sleeping...')
        await asyncio.sleep(parse_timeout)
