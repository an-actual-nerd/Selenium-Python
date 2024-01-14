import pytest

@pytest.fixture(scope="module")
def setup():
    print("Creating DB")

    yield
    print("Ending DB")


@pytest.fixture(scope="function")
def before():
    print("Opening Browser")

    yield
    print("Closing Browser")

def test_dologin(setup, before):
    print("Executing login test")

def test_userreg(setup, before):
    print("Executing user Reg test")