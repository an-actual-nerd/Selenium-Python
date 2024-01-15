import pytest

def get_data():

    return [
        ("me@automation.com", "12345789"),
        ("you@automation.com", "87654321"),
        ("python@automation.com", "003456")
    ]

@pytest.mark.parametrize("username, password", get_data())
def test_login(username, password):
    print(username, "--------", password)