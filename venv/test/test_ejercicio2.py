from src.ejercicio2 import anos

def test_anos():
    assert anos(5) == ["Tienes 1 años", "Tienes 2 años", "Tienes 3 años", "Tienes 4 años", "Tienes 5 años"]
    assert anos(0) == []
    assert anos(1) == ["Tienes 1 años"]