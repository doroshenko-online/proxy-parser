import argparse
from multiprocessing import Process
import os

from yaml import load, CLoader
import yaml

from proxy.entrypoints import entrypoint_parser
from proxy.helpers.logger import log
from proxy.models.registry import DriversEnum

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", help='path to root project directory')
    parser.add_argument("--conf", help='path to config file')
    parser.add_argument("--gecko", action='store_true', help='Use geckodriver. Chromedriver is default')
    args = parser.parse_args()


    # init paths
    path = args.path
    if path is not None:
        main_path = os.path.abspath(path)
    else:
        log('path not found in args', 'error')
        raise Exception

    static_path =os.path.join(main_path, 'static')

    if args.gecko:
        use_driver = DriversEnum.gecko.value
    else:
        use_driver = DriversEnum.chrome.value

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
    parser_process = Process(target=entrypoint_parser, kwargs={'static': static_path, 'chrome': chrome_driver, 'gecko': gecko_driver, 'use_driver': use_driver, 'conf': conf})
    parser_process.start()
