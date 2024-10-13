# hook function. works similar to fixture function

# def setup_function(function):
def setup_module(module):
    print("open browser")


# def teardown_function(function):
def teardown_module(module):
    print("close browser")


def test_one_method():
    print("printing one method")


def test_two_method():
    print("printing two method")


def test_three_method():
    print("printing three method")
