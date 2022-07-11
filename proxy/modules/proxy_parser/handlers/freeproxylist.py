from typing import List

import aiohttp
from proxy.models.proxy import ProxyModel
from proxy.modules.proxy_parser.handlers.base import BaseProxyParser


class FreeProxyList(BaseProxyParser):

    available_protocols = ['http', 'https']
    default_query_params = '/ru/?pr={protocol}&u=10&page={page_num}'
    

    async def run(self) -> None:
        async with aiohttp.ClientSession() as session:
            for protocol in self.available_protocols:
                protocol = protocol.upper()
                first_page = f'{self.resource_model.addr}/{self.default_query_params.format(protocol=protocol, page_num=1)}'
                async with session.get(first_page, headers=self.user_agent) as resp:
                    print(resp.status)
                    print(await resp.text())
                break

    def extract_proxy_from_content(self, content: str) -> List[ProxyModel]:
        pass

    def get_pages_count(self, content: str) -> int:
        pass

    async def get_content(self) -> str:
        pass