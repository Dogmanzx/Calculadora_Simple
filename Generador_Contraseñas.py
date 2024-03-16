import string
import random

def generador_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    return contraseña

print(generador_contraseña(10))
