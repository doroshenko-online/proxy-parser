from proxy.helpers.logger import log
from proxy.models.registry import Registry, DriversEnum


def entrypoint(*args, **kwargs) -> None:
    """
    Entrypoint for parser process
    """
    Registry.static_path = kwargs.get('static')
    chrome_path = kwargs.get('chrome')
    gecko_path = kwargs.get('gecko')
    use_driver = kwargs.get('use_driver')
    if not use_driver:
        log('Driver not set', 'error')
        raise Exception

    Registry.drivers[DriversEnum.chrome.value] = chrome_path
    Registry.drivers[DriversEnum.gecko.value] = gecko_path

    try:
        Registry.driver = Registry.drivers[use_driver]
    except KeyError:
        log('Driver path is not available', 'error')
        raise Exception
    pass
