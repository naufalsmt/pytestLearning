import pytest


@pytest.mark.smoke
def test_four():
    print("four test")


@pytest.mark.regression
def test_five():
    print("five test")
