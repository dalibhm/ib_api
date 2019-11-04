import os
from datetime import datetime
from glob import glob

import re

# TIME_FORMAT = '%Y-%m-%d %H:%M:%S.%f'
TIME_FORMAT = '%Y%m%d_%H%M%S'


def get_latest(files, pattern):
    regex = re.compile(pattern)
    dates_str = [regex.search(file).group(1) for file in files]
    dates = [datetime.strptime(date_str, TIME_FORMAT) for date_str in dates_str]
    most_recent_date = max(dates)
    most_recent_file = pattern.replace('(.*)', datetime.strftime(most_recent_date, TIME_FORMAT))
    return most_recent_file


def check_for_new_content(latest_file, report_content):
    with open(latest_file, "r") as file_reader:
        existent_content = file_reader.read()
    return existent_content.replace('\r', '') == report_content.replace('\r', '')


class FileManager:
    def __init__(self, base_directory):
        self.base_directory = base_directory

    def process_report(self, symbol, report_type, report_content):
        report_already_downloaded = self.check_if_already_downloaded(symbol, report_type, report_content)
        if not report_already_downloaded:
            self.save_report(symbol, report_type, report_content)

    def get_latest_report_date(self, symbol, report_type):
        file_pattern = os.path.join(self.base_directory, '{}_{}*.xml'.format(symbol, report_type))
        files = glob(file_pattern)
        if not len(files) > 0:
            return ''
        else:
            re_pattern = os.path.join(self.base_directory, '{}_{}_(.*).xml'.format(symbol, report_type))
            regex = re.compile(re_pattern)
            dates_str = [regex.search(file).group(1) for file in files]
            dates = [datetime.strptime(date_str, TIME_FORMAT) for date_str in dates_str]
            most_recent_date = max(dates)
            return datetime.strftime(most_recent_date, '%Y-%m-%d')

    def check_if_already_downloaded(self, symbol, report_type, report_content):
        # os.chdir(self.base_directory)
        pattern = os.path.join(self.base_directory, '{}_{}*.xml'.format(symbol, report_type))
        files = glob(pattern)
        if not len(files) > 0:
            return False
        else:
            re_pattern = os.path.join(self.base_directory, '{}_{}_(.*).xml'.format(symbol, report_type))
            latest_file = get_latest(files, re_pattern)
            content_has_changed = check_for_new_content(latest_file, report_content)
            return content_has_changed

    def save_report(self, symbol, report_type, report_content):
        filename = '{}_{}_{}.xml'.format(symbol, report_type, datetime.strftime(datetime.now(), TIME_FORMAT))
        full_path = os.path.join(self.base_directory, filename)
        with open(full_path, "w") as file_writer:
            file_writer.write(report_content)
