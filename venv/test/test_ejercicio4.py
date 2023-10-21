from src.ejercicio4 import  cuantatras

def test_cuantatras():
    assert cuantatras(5) == [5, 4, 3, 2, 1, 0]
    assert cuantatras(0) == [0]
    assert cuantatras(1) == [1, 0]