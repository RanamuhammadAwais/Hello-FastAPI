from youtube import main

def test_function1():
    r = main.my_first_function()
    assert r == "hello world"



def test_function2():
    r = main.my_first_function()
    assert r != "paksitanpoet"
