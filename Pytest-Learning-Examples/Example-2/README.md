# Pytest- Test Fixture

### What are test fixtures

• Fixtures are functions, which will run before each test function to which it is applied. 

• Instead of running the same code for every test, we can attach fixture function to the tests and it will run and return the data to the test before executing each test.

#### Fixtures can be applied in 2 levels

1. **Function level-** This will be executed at every testcase function.
2. **Module Level-** This will be executed at the start and the at the end of every test case has been executed.

### Function level

• To create a fixture, a setup function is first created.
```commandline
def setup_function(function):
    print("Opening Browser")
```

• A tear down function is created.
```commandline
def teardown_function(function):
    print("Closing the browser")
```

### Module Level

• Same as function level, setup and tear down function is create.
```commandline
def setup_module(module):
    print("Creating DB")

def teardown_module(module):
    print("Ending DB")
```

# Full Code
```commandline
import pytest

# Fixture at module level
def setup_module(module):
    print("Creating DB")

def teardown_module(module):
    print("Ending DB")

# Fixture at function level
def setup_function(function):
    print("Opening Browser")

def teardown_function(function):
    print("Closing the browser")

def test_dologin():
    print("Executing login test")

def test_userreg():
    print("Executing user Reg test")
```