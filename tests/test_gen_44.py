from app.gen_44 import value_44


def test_value_44():
    assert value_44(2) == 2 * 3 + 5
    assert value_44(0) == 5
