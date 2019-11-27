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
    return most_recent_date, most_recent_file


def check_for_new_content(latest_file, report_content):
    with open(latest_file, "r") as file_reader:
        existent_content = file_reader.read()
    return existent_content.replace('\r', '') == report_content.replace('\r', '')


class FileManager:
    @classmethod
    def init_directory(cls, base_directory):
        cls.base_directory = base_directory

    @classmethod
    def process_report(cls, symbol, report_type, report_content):
        report_already_downloaded = cls.check_if_already_downloaded(symbol, report_type, report_content)
        if not report_already_downloaded:
            cls.save_report(symbol, report_type, report_content)

    @classmethod
    def get_latest_report(cls, symbol, report_type):
        file_pattern = os.path.join(cls.base_directory, '{}_{}*.xml'.format(symbol, report_type))
        files = glob(file_pattern)
        if not len(files) > 0:
            return ''
        else:
            re_pattern = os.path.join(cls.base_directory, '{}_{}_(.*).xml'.format(symbol, report_type))
            latest_date, latest_file = get_latest(files, re_pattern)
            return latest_date, latest_file

    @classmethod
    def check_if_already_downloaded(cls, symbol, report_type, report_content):
        # os.chdir(self.base_directory)
        _, latest_file = cls.get_latest_report(symbol, report_type)
        content_has_changed = check_for_new_content(latest_file, report_content)
        return content_has_changed

    @classmethod
    def save_report(cls, symbol, report_type, report_content):
        filename = '{}_{}_{}.xml'.format(symbol, report_type, datetime.strftime(datetime.now(), TIME_FORMAT))
        full_path = os.path.join(cls.base_directory, filename)
        with open(full_path, "w") as file_writer:
            file_writer.write(report_content)


if __name__ == '__main__':
    file_manager = FileManager('/Users/dali/workspace/ib_python/fundamental_data/data')
    latest = file_manager.get_latest_report_date(symbol='AA', report_type='ReportsFinStatements')
    print(latest)