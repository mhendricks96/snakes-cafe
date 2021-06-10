from snakes_cafe import __version__
from snakes_cafe.snakes_cafe import addChoice


def test_version():
    assert __version__ == '0.1.0'

def test_wrong_item():
    actual = addCoice("michael")
    expected = "sorry, please choose something on the menu"
    assert actual == expected