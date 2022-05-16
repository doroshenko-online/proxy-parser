from enum import IntEnum
from typing import List, Union

from models.proxy import Proxy


class ProxyProtocols(IntEnum):
    HTTP = 1
    HTTPS = 2
    SOCKS4 = 3
    SOCKS5 = 4



class BaseProxyParser:

    target_url = None


    async def get_main_page_content(self) -> Union(str, None):
        pass

    @classmethod
    async def get_content(cls, url: str) -> Union(str, None):
        pass

    @classmethod
    def extract_proxy_from_content(cls, content: str) -> List[Proxy]:
        pass
