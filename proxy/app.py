import argparse
from multiprocessing import Process
import os

from yaml import load, CLoader
import yaml

from proxy.entrypoints.parse_proxies import entrypoint
from proxy.helpers.logger import log

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--path")
    parser.add_argument("--conf")
    args = parser.parse_args()

    # init paths
    path = args.path
    if path is not None:
        main_path = os.path.abspath(path)
    else:
        log('path not found in args', 'error')
        raise Exception

    static_path =os.path.join(main_path, 'static')

    selenium_drivers_path = os.path.join(main_path, 'selenium_drivers')

    chrome_driver = os.path.join(selenium_drivers_path, 'chromedriver')  # ver. 101
    if not os.path.exists(chrome_driver):
        log('chrome driver path is not available', 'error')
        raise Exception

    gecko_driver = os.path.join(selenium_drivers_path, 'geckodriver')  # ver. 0.32
    if not os.path.exists(gecko_driver):
        log('gecko driver path is not available', 'error')
        raise Exception

    # load config
    conf_file = open(args.conf, 'r')
    conf = yaml.load(conf_file, CLoader)

    log('Run parser process', 'info')
    parser_process = Process(target=entrypoint, kwargs={'static': static_path, 'chrome': chrome_driver, 'gecko': gecko_driver, 'use_driver': 1})
    parser_process.start()
