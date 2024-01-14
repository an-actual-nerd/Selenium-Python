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