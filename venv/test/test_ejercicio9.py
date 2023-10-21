from src.ejercicio9 import contraseña

def test_contraseña():
    assert contraseña("contraseña") == "Contraseña correcta. Acceso permitido."
    