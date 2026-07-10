from app.gen_25 import value_25


def test_value_25():
    assert value_25(2) == 2 * 4 + 5
    assert value_25(0) == 5
