from src.ejercicio8 import numero

def test_numero():
    assert numero(5) == "1 \n3 1 \n5 3 1 \n"
    assert numero(0) == ""
    assert numero(1) == "1 \n"