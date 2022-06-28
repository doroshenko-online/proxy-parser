from enum import Enum, IntEnum

from proxy.modules.proxy_parser.handlers import freeproxylist, geonode, git_fate0, hidemyname, proxy_searcher


class TimeoutEnum(Enum):
    s = 1
    m = 60
    h = 3600
    d = 3600 * 24


class ParserHandlersEnum(Enum):
    freeproxylist = freeproxylist.FreeProxyList
    geonode = geonode.Geonode
    git_fate0 = git_fate0.Gitfate
    hidemyname = hidemyname.HideMyName
    proxy_searcher = proxy_searcher.ProxySearcher


class ProxyProtocols(IntEnum):
    HTTP = 1
    HTTPS = 2
    SOCKS4 = 3
    SOCKS5 = 4