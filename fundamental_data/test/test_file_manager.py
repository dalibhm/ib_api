import os
import sys

module_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(module_dir, '..'))

from file_manager import FileManager


def test_check_if_downloaded_false():
    file_manager = FileManager('./data')
    is_downloaded = file_manager.check_if_already_downloaded('PAYC', 'ReportsFinStatements', '')
    assert False == is_downloaded


def test_check_if_downloaded_true():
    file = '/Users/dali/workspace/fundamental_data/data/SHOP_ReportsFinSummary_2019-10-25 19:06:36.699338.xml'
    with open(file, "r") as file_reader:
        content = file_reader.read()
    file_manager = FileManager('./data')
    is_downloaded = file_manager.check_if_already_downloaded('SHOP', 'ReportsFinStatements', content)
    assert False == is_downloaded
