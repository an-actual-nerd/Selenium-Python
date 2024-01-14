# Markers

• Markers are used to send some meta data on a unit test function.

• It is also used to skip the execution of some specific test cases.

### Marker file

• Create an ini file name pytest and define the markers in that file.

• This helps to create custom markers for our test.
```commandline
[pytest]
markers =
            functional
            regressional
```

# How to execute

### To execute functional
```commandline
pytest .\test_Markers.py -s -v -m "functional"
```

### To execute non functional
```commandline
pytest .\test_Markers.py -s -v -m "not functional"
```

# Full code

```commandline
import pytest

@pytest.mark.functional
def test_login():
    print("Execution login user")

@pytest.mark.regressional
def test_user_reg():
    print("Executing user reg")

@pytest.mark.functional
def test_compose_email():
    print("Composing mail")
```