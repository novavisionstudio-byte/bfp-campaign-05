from app.gen_4 import value_4


def test_value_4():
    assert value_4(2) == 2 * 8 + 2
    assert value_4(0) == 2
