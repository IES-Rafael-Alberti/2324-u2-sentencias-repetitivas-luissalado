from src.ejercicio6 import triangulo


def test_triangulo():
    assert triangulo(5) == "*\n**\n***\n****\n*****\n"
    assert triangulo(0) == ""
    assert triangulo(1) == "*\n"