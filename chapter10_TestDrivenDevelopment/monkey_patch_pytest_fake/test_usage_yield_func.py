import pytest

@pytest.yield_fixture()
def patch_something():
    print("patch!")
    yield
    print("remove patch!")

def test_dosomething(patch_something):
    print("dosomething")