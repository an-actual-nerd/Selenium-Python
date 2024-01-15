# Pytest- Test Fixture with Decorators

• Fixtures can also be done with decorators.

### For function Level
```commandline
@pytest.fixture(scope="function")
def before():
    print("Opening Browser")

    yield
    print("Closing Browser")
```

### Module Level

```commandline
@pytest.fixture(scope="module")
def setup():
    print("Creating DB")

    yield
    print("Ending DB")
```

# Full Source Code

```commandline
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
```