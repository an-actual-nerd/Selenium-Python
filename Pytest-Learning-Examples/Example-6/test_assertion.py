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