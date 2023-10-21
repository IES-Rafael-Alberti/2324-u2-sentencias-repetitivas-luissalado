from src.ejercicio3 import comprobarpar

def test_comprobarpar():
    assert comprobarpar(10) == [1, 3, 5, 7, 9]
    assert comprobarpar(5) == [1, 3]
    assert comprobarpar(1) == []