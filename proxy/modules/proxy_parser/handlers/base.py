from typing import List

from proxy.models.proxy import ProxyModel


class BaseProxyParser:

    user_agent = {'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

    def __init__(self, resource_model) -> None:
        self.resource_model = resource_model


    async def run(self) -> None:
        pass

    def extract_proxy_from_content(cls, content: str) -> List[ProxyModel]:
        pass
