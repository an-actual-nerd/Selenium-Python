# Paramertize Marker

• Parameterize marker help us to use data which are present in multiple data set.

• N number of test can be iterated.

• Created a function for dummy dataset
```commandline
def get_data():

    return [
        ("me@automation.com", "12345789"),
        ("you@automation.com", "87654321"),
        ("python@automation.com", "003456")
    ]
```

# Full Code
```commandline
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
```