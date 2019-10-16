from configparser import ConfigParser
import json
import os

from runner.runner_manager import RunnerManager


def main():
    config = ConfigParser()
    config.read('./settings/development.ini')
    filename = config['data config']['file']
    with open(os.path.join('.', 'settings', filename), 'r') as f:
        data_config = json.load(f)
    runner_manager = RunnerManager(data_config)


if __name__ == 'main':
    main()