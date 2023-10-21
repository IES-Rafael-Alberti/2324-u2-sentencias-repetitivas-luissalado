from src.ejercicio12 import analiza

def test_analiza():
    assert analiza("Hola", "o") == 1
    assert analiza("Esta frase", "a") == 2
    assert analiza("Test", "z") == 0