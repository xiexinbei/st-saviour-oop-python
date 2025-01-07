from sanrio import Sanrio
from hellokittyfamily import HelloKittyFamily
from kittywhite import KittyWhite

def test_kitty_white():
    kw = KittyWhite('apple pie', 'no mouth')

    assert kw.location == 'United Kingdom'
    assert kw.help_others() == 'KittyWhite from United Kingdom wants to make friends with you!'

    assert isinstance(kw, Sanrio)
    assert isinstance(kw, HelloKittyFamily)
    assert isinstance(kw, KittyWhite)
