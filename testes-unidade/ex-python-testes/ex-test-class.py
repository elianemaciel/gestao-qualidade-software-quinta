import pytest

class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

@pytest.fixture
def my_class():
    return MyClass(name="pavol", age=39)

def test_name(my_class):
    assert my_class.name == "pavol"

def test_age(my_class):
    assert my_class.age == 39