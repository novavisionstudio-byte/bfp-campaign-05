from app.gen_43 import value_43


def test_value_43():
    assert value_43(2) == 2 * 7 + 2
    assert value_43(0) == 2
