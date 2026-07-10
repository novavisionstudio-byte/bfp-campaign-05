from app.gen_7 import value_7


def test_value_7():
    assert value_7(2) == 2 * 3 + 5
    assert value_7(0) == 5
