import pytest


@pytest.mark.regression
def test_one():
    print("first test")


@pytest.mark.skip
def test_two():
    print("two test")


@pytest.mark.smoke
def test_three():
    print("three test")
