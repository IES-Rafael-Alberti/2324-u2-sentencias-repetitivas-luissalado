from src.ejercicio11 import contar

def test_contar():
    assert contar("hola") == "a\nl\no\nh\n"
    assert contar("python") == "n\no\th\nt\ny\np\n"
    assert contar("") == ""