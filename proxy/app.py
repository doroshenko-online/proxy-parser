import argparse
from datetime import datetime
from multiprocessing import Process
import os

from yaml import load, CLoader
import yaml

from proxy.cron.parse_proxies import entrypoint

def log(message, level):
    now = datetime.utcnow()
    print(f"[{now}] [{level}]: {message}")

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
        raise Exception('path not found in args')

    static_path =os.path.join(main_path, 'static')

    selenium_drivers_path = os.path.join(main_path, 'selenium_drivers')

    chrome_driver = os.path.join(selenium_drivers_path, 'chromedriver')  # ver. 101
    gecko_driver = os.path.join(selenium_drivers_path, 'geckodriver')  # ver. 0.32

    # load config
    conf_file = open(args.conf, 'r')
    conf = yaml.load(conf_file, CLoader)

    parser_process = Process(target=entrypoint)
    parser_process.start()
