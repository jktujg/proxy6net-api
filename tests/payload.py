from src.proxy6net_api.types import Proxy6Proxy
from typing import Literal


def fake_proxy(id: str, type: Literal['http', 'socks'] = 'http'):
    return Proxy6Proxy(**{
        'id': id,
        'ip': "2a00:1838:32:198:56ec:2696::386",
        'host': "185.22.134.242",
        'port': "7386",
        'user': "nV5TFK",
        'pass': "3Itr1t",
        'type': type,
        'country': "ru",
        'date': "2016-06-27 16:06:22",
        'date_end': "2016-07-11 16:06:22",
        'unixtime': 1466379159,
        'unixtime_end': 1468349441,
        'descr': "",
        'active': "1",
        }
                       )
