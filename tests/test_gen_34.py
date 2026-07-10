from app.gen_34 import value_34


def test_value_34():
    assert value_34(2) == 2 * 3 + 3
    assert value_34(0) == 3
