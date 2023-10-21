from src.ejercicio10 import es_primo

def test_es_primo():
    assert not es_primo(0)
    assert not es_primo(1)
    assert es_primo(2)
    assert es_primo(3)







