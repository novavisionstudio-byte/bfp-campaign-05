from app.gen_33 import value_33


def test_value_33():
    assert value_33(2) == 2 * 7 + 3
    assert value_33(0) == 3
