import argparse
from datetime import datetime
from multiprocessing import Process
import os

from yaml import load, CLoader
import yaml

def log(message, level):
    now = datetime.utcnow()
    print(f"[{now}] [{level}]: {message}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--path")
    parser.add_argument("--conf")
    args = parser.parse_args()

    path = args.path
    static_path =os.path.join(path, 'static')

    conf_file = open(args.conf, 'r')
    conf = yaml.load(conf_file, CLoader)
