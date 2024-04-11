# content of test_sample.py
def func(x):
    return x * 1


def test_answer():
    assert func(3) == 3


def test_answer_two():
    assert func("2") == 4


func("3")
