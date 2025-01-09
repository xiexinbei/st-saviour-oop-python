from sanrio import Sanrio
from hellokittyfamily import HelloKittyFamily
from kittywhite import KittyWhite
from georgewhite import GeorgeWhite

def test_kitty_white():
    kw = KittyWhite('apple pie', 'no mouth')

    assert kw.location == 'United Kingdom'
    assert kw.help_others() == 'KittyWhite from United Kingdom wants to make friends with you!'

    assert isinstance(kw, Sanrio)
    assert isinstance(kw, HelloKittyFamily)
    assert isinstance(kw, KittyWhite)

def test_george_white():
    gw = GeorgeWhite('engineer')

    assert gw.work() == 'Let\'s work with George!'