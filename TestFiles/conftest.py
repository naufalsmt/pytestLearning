import pytest


@pytest.fixture(autouse=True, scope="session")
def setup_and_teardown():
    print("open 1")
    print("open 2")
    yield
    print("quite")
