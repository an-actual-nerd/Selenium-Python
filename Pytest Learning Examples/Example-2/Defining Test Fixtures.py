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