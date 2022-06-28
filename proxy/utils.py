from proxy.enums import TimeoutEnum


def get_timeout_from_config_value(conf_value: str) -> int:
    timeout_type = conf_value[-1]
    return int(conf_value[0:-1]) * getattr(TimeoutEnum, timeout_type).value