# noinspection PyPackageRequirements
import pytest

import sys
import os

container_folder = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..'
))
sys.path.insert(0, container_folder)



from app import create_app


@pytest.fixture
def client():
    app = create_app('testing')
    app_context = app.app_context()
    app_context.push()

    client = app.test_client()

    yield client
