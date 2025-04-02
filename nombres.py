nombre = str(input("< ernesto >/n")) #str
edad = int(input("<16 > /n")) # int
comida = int(input("< crepas /n")) # int
cuidad = int(input("< Guadalajara > /n")) # int

escribe_fichero (nombre)
escribe_fichero (edad)
escribe_fichero (comida)
escribe_fichero (cuidad)

def escribe_fichero(mensaje):
    with open('fichero_comunicacion.txt', 'w') as fichero:
        fichero.write(mensaje)

def lee_fichero():
    mensaje = ""
    with open('fichero_comunicacion.txt', 'r') as fichero
    mensaje = fichero.read()

    return mensaje

escribe_fichero('Esto es un mensaje')
print(lee_fichero)      