from app.gen_42 import value_42


def test_value_42():
    assert value_42(2) == 2 * 9 + 9
    assert value_42(0) == 9
