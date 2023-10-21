from src.ejercicio17 import sumadigitos

def test_sumadigitos():
    assert sumadigitos(123) == 6
    assert sumadigitos(456) == 15
    assert sumadigitos(789) == 24
    assert sumadigitos(111) == 3