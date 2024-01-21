# Pytest Assertions

### What is soft assertions

• Assertion is used to check if certain condition in your code are true.

### There are two types of assertions.

**1). Hard Assertions**

• Code stops functioning as soon as it hits any red flags/erros.

• The rest of the tescase will not executed.

**2). Soft Assertions**

• All the test cases will be executed and results will be printed in a tabular manner.

```commandline
E           AssertionError: 
E           +----------------------+-----------------+---------------+---------------------+
E           |      expression      |    condition    | current value |      expected       |
E           +======================+=================+===============+=====================+
E           | assert               | ==              | Google.com    | Youtube.com         |
E           | expected_titile ==   |                 |               |                     |
E           | actual_title         |                 |               |                     |
E           +----------------------+-----------------+---------------+---------------------+
E           | assert 'Gmails' in   | in              | Gmails        | in This is a gmail  |
E           | title                |                 |               | site                |
E           +----------------------+-----------------+---------------+---------------------+
E           | assert (False)       | <Not condition> | False         | <Not None>        
```

### Comands to Run the code
```commandline
Go the the file directory

pytest .\test_assertion.py -s -v --soft-asserts
```

# Full Code

```commandline
import pytest

def test_validate_titile():

    # Hard assertion

    expected_titile = "Google.com"
    actual_title = "Youtube.com"
    title = "This is a gmail site"

    # Soft Assertion

    assert expected_titile == actual_title
    assert "Gmails" in title, "Gmail does not exist in the title."
    assert False, "Forcefully failing the test"
```