from bank import value


def test_greeting():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("hi world") == 20
    assert value("HI WORLD") == 20
    assert value("wassup world") == 100
    assert value("WASSUP WORLD") == 100
