from twttr import shorten

def test_shorten ():
    assert shorten ("twitter") == "twttr"
    assert shorten ("TWITTER") == "TWTTR"
    assert shorten ("tw1tt3r") == "tw1tt3r"
    assert shorten ("tw!tt&r") == "tw!tt&r"


