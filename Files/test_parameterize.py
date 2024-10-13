import pytest

@pytest.mark.parametrize('username, password',[("arun", "1234"), ("varun", "1234"),("tharun", "1234")])
def test_credential_test(username, password):
    print(username+"-"+password)
