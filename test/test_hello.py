from hello import hello

def test_default():
    assert hello("David") == "Hello, David"

def test_argument():
    assert hello() == 'Hello, world'
    
