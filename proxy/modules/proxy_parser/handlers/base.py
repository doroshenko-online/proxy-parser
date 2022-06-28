from typing import List

from proxy.models.proxy import ProxyModel


class BaseProxyParser:

    model = None


    async def run(self) -> None:
        pass

    def extract_proxy_from_content(cls, content: str) -> List[ProxyModel]:
        pass
