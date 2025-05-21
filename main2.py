'''
from LaberintoBuilder.director import Director
from Ente.personaje import Personaje
import os
import sys

# Para evitar errores de recursión
nombre = input("Nick del personaje: ")
personaje = Personaje()

opcion = input("Opción de juego:\n    1. Jugar\n    2. Salir\nSelecciona una opción: ")

jsons = os.listdir('json/')
print("JSON disponibles:")
for idx, json_file in enumerate(jsons):
    print(f"    {idx}. {json_file}")

while opcion not in ["1", "2"]:
    print("Opción inválida. Por favor, selecciona una opción válida (1 o 2).")
    opcion = input("Opción de juego:\n    1. Jugar\n    2. Salir\nSelecciona una opción: ")

if opcion == "2":
    sys.exit()

json_idx = input("Selecciona un json: ")
while not json_idx.isdigit() or int(json_idx) < 0 or int(json_idx) >= len(jsons):
    print("Selección inválida. Introduce un número válido correspondiente al JSON.")
    json_idx = input("Selecciona un json: ")

json_file = jsons[int(json_idx)]

director = Director()
director.procesar(os.path.join('json', json_file))
juego = director.getJuego()
forma = director.form
personaje.seudonimo = nombre
juego.agregarPersonaje(personaje)
juego.prota = personaje
print(forma)

while not juego.fase.esFinal():
    if forma == "Cuadrado":
        print("\n¿Qué deseas hacer?\n    A. Atacar\n    1. Mover al norte\n    2. Mover al este\n    3. Mover al oeste\n    4. Mover al sur\n",
              "   5. Abrir Puertas\n    6. Lanzar bichos\n    7. Mostrar comandos bolsa\n    8. Mostrar comandos cuerpo\n",   
              "   H. Obtener objetos de la posición del personaje\n    C. Obtener Comandos\n    I. Mostrar inventario")
    elif forma == "Rombo":
        print("\n¿Qué deseas hacer?\n    A. Atacar\n    1. Mover al noreste\n    2. Mover al noroeste\n    3. Mover al sureste\n    4. Mover al suroeste\n",
              "   5. Abrir Puertas\n    6. Lanzar bichos\n    7. Mostrar comandos bolsa\n    8. Mostrar comandos cuerpo\n",
              "   H. Obtener objetos de la posición del personaje\n    C. Obtener Comandos\n    I. Mostrar inventario")
    elif forma == "Hexagono":
        print("\n¿Qué deseas hacer?\n    A. Atacar\n    1. Mover al norte\n    2. Mover al sur\n    3. Mover al noreste\n    4. Mover al noroeste\n",
              "   5. Mover al sureste\n    6. Mover al suroeste\n    7. Abrir Puertas\n    8. Lanzar bichos\n    9. Mostrar comandos bolsa\n",
              "   10. Mostrar comandos cuerpo\n    H. Obtener objetos de la posición del personaje\n    C. Obtener Comandos\n    I. Mostrar inventario")

    sys.stdin.flush()
    eleccion = input("Ingresa tu elección: ")

    if eleccion == "1":
        if forma == "Cuadrado":
            personaje.irAlNorte()
        elif forma == "Rombo":
            personaje.irAlNoreste()
        elif forma == "Hexagono":
            personaje.irAlNorte()

    elif eleccion == "2":
        if forma == "Cuadrado":
            personaje.irAlEste()
        elif forma == "Rombo":
            personaje.irAlNoroeste()
        elif forma == "Triangulo":
            personaje.irAlSur()

    elif eleccion == "3":
        if forma == "Cuadrado":
            personaje.irAlOeste()
        elif forma == "Rombo":
            personaje.irAlSureste()
        elif forma == "Hexagono":
            personaje.irAlNoreste()

    elif eleccion == "4":
        if forma == "Cuadrado":
            personaje.irAlSur()
        elif forma == "Rombo":
            personaje.irAlSuroeste()
        elif forma == "Hexagono":
            personaje.irAlNoroeste()
        else:
            juego.openDoors() # Si es triangulo la opcion es abrir puertas

    elif eleccion == "5":
        if forma == "Hexagono":
            personaje.irAlSureste()
        else:
            juego.openDoors()

    elif eleccion == "6":
        if forma == "Hexagono":
            personaje.irAlSuroeste()
        else:
            juego.fabricarBichoAgresivo(2)

    elif eleccion == "7":
        if forma == "Hexagono":
            juego.openDoors()
        
        else:
            coms = personaje.mochila.obtenerComandos(personaje)
            if len(coms) > 0:
                print("Comandos disponibles:")
                for idx, com in enumerate(coms):
                    print(f"    {idx}. {com}")
                el = input("Selecciona un comando (número): ")
                while not el.isdigit() or int(el) < 0 or int(el) >= len(coms):
                    print("Selección inválida. Introduce un número válido correspondiente al comando.")
                    el = input("Selecciona un comando (número): ")
                coms[int(el)].ejecutar(personaje)
            else:
                print("No hay objetos en la bolsa.")
    
    elif eleccion.lower() == "8":
        if forma == "Hexagono":
            juego.fabricarBichoAgresivo(2)

    elif eleccion.lower() == "a":
        personaje.atacar()

    elif eleccion.lower() == "i":
        print("Inventario:")
        if len(personaje.mochila.children) > 0:
            for idx, obj in enumerate(personaje.mochila.children):
                print(f"    {idx}. {obj}")
            el = input("Selecciona un objeto (número): ")
            while not el.isdigit() or int(el) < 0 or int(el) >= len(personaje.mochila.children):
                print("Selección inválida. Introduce un número válido correspondiente al objeto.")
                el = input("Selecciona un objeto (número): ")
            
            coms = personaje.mochila.children[int(el)].obtenerComandos(personaje)
            if len(coms) > 0:
                print("Comandos disponibles:")
                for idx, com in enumerate(coms):
                    print(f"    {idx}. {com}")
                ele = input("Selecciona un comando (número): ")
                while not ele.isdigit() or int(ele) < 0 or int(ele) >= len(coms):
                    print("Selección inválida. Introduce un número válido correspondiente al comando.")
                    ele = input("Selecciona un comando (número): ")
                coms[int(ele)].ejecutar(personaje)
            else:
                print("No hay comandos disponibles para este objeto.")
        else:
            print("No hay objetos en la mochila.")

    elif eleccion.lower() == "h":
        hijos = juego.getChildrenPosition()
        if len(hijos) > 0:
            print("Objetos disponibles:")
            for idx, hijo in enumerate(hijos):
                print(f"    {idx}. {hijo}")
            el = input("Selecciona un objeto (número): ")
            while not el.isdigit() or int(el) < 0 or int(el) >= len(hijos):
                print("Selección inválida. Introduce un número válido correspondiente al objeto.")
                el = input("Selecciona un objeto (número): ")
            hijos[int(el)].entrar(personaje)
        else:
            print("No hay objetos en la sala.")

    elif eleccion.lower() == "c":
        coms = personaje.obtenerComandos(personaje)
        if len(coms) > 0:
            print("Comandos disponibles:")
            for idx, com in enumerate(coms):
                print(f"    {idx}. {com}")
            el = input("Selecciona un comando (número): ")
            while not el.isdigit() or int(el) < 0 or int(el) >= len(coms):
                print("Selección inválida. Introduce un número válido correspondiente al comando.")
                el = input("Selecciona un comando (número): ")
            coms[int(el)].ejecutar(personaje)
        else:
            print("No hay comandos disponibles.")
'''


from LaberintoBuilder.director import Director
from Ente.personaje import Personaje
import os
import sys

nombre = input("Nick del personaje: ")
personaje = Personaje()

opcion = input("Opción de juego:\n    1. Jugar\n    2. Salir\nSelecciona una opción: ")

jsons = os.listdir('json/')
print("JSON disponibles:")
for idx, json_file in enumerate(jsons):
    print(f"    {idx}. {json_file}")

while opcion not in ["1", "2"]:
    print("Opción inválida. Por favor, selecciona una opción válida (1 o 2).")
    opcion = input("Opción de juego:\n    1. Jugar\n    2. Salir\nSelecciona una opción: ")

if opcion == "2":
    sys.exit()

json_idx = input("Selecciona un json: ")
while not json_idx.isdigit() or int(json_idx) < 0 or int(json_idx) >= len(jsons):
    print("Selección inválida. Introduce un número válido correspondiente al JSON.")
    json_idx = input("Selecciona un json: ")

json_file = jsons[int(json_idx)]

director = Director()
director.procesar(os.path.join('json', json_file))
juego = director.getJuego()
forma = director.form
personaje.seudonimo = nombre
juego.agregarPersonaje(personaje)
juego.prota = personaje
print(forma)

while not juego.fase.esFinal():
    if forma == "Cuadrado":
        print("\n¿Qué deseas hacer?\n    A. Atacar\n    1. Mover al norte\n    2. Mover al este\n    3. Mover al oeste\n    4. Mover al sur\n"
              "   5. Abrir Puertas\n    6. Lanzar bichos\n    7. Mostrar comandos bolsa\n    8. Mostrar comandos cuerpo\n"
              "   H. Obtener objetos de la posición del personaje\n    C. Obtener Comandos\n    I. Mostrar inventario")
    elif forma == "Rombo":
        print("\n¿Qué deseas hacer?\n    A. Atacar\n    1. Mover al noreste\n    2. Mover al noroeste\n    3. Mover al sureste\n    4. Mover al suroeste\n"
              "   5. Abrir Puertas\n    6. Lanzar bichos\n    7. Mostrar comandos bolsa\n    8. Mostrar comandos cuerpo\n"
              "   H. Obtener objetos de la posición del personaje\n    C. Obtener Comandos\n    I. Mostrar inventario")
    elif forma == "Hexagono":
        print("\n¿Qué deseas hacer?\n    A. Atacar\n    1. Mover al norte\n    2. Mover al sur\n    3. Mover al noreste\n    4. Mover al noroeste\n"
              "   5. Mover al sureste\n    6. Mover al suroeste\n    7. Abrir Puertas\n    8. Lanzar bichos\n    9. Mostrar comandos bolsa\n"
              "   10. Mostrar comandos cuerpo\n    H. Obtener objetos de la posición del personaje\n    C. Obtener Comandos\n    I. Mostrar inventario")

    sys.stdin.flush()
    eleccion = input("Ingresa tu elección: ")

    if forma == "Hexagono":
        if eleccion == "1": personaje.irAlNorte()
        elif eleccion == "2": personaje.irAlSur()
        elif eleccion == "3": personaje.irAlNoreste()
        elif eleccion == "4": personaje.irAlNoroeste()
        elif eleccion == "5": personaje.irAlSureste()
        elif eleccion == "6": personaje.irAlSuroeste()
        elif eleccion == "7": juego.openDoors()
        elif eleccion == "8": juego.fabricarBichoAgresivo(2)
        elif eleccion == "9": coms = personaje.mochila.obtenerComandos(personaje)
        elif eleccion == "10": coms = personaje.obtenerComandos(personaje)

    elif forma == "Cuadrado":
        if eleccion == "1": personaje.irAlNorte()
        elif eleccion == "2": personaje.irAlEste()
        elif eleccion == "3": personaje.irAlOeste()
        elif eleccion == "4": personaje.irAlSur()
        elif eleccion == "5": juego.openDoors()
        elif eleccion == "6": juego.fabricarBichoAgresivo(2)
        elif eleccion == "7": coms = personaje.mochila.obtenerComandos(personaje)
        elif eleccion == "8": coms = personaje.obtenerComandos(personaje)

    elif forma == "Rombo":
        if eleccion == "1": personaje.irAlNoreste()
        elif eleccion == "2": personaje.irAlNoroeste()
        elif eleccion == "3": personaje.irAlSureste()
        elif eleccion == "4": personaje.irAlSuroeste()
        elif eleccion == "5": juego.openDoors()
        elif eleccion == "6": juego.fabricarBichoAgresivo(2)
        elif eleccion == "7": coms = personaje.mochila.obtenerComandos(personaje)
        elif eleccion == "8": coms = personaje.obtenerComandos(personaje)

    elif eleccion.lower() == "a":
        personaje.atacar()

    elif eleccion.lower() == "h":
        hijos = juego.getChildrenPosition()
        if hijos:
            for idx, hijo in enumerate(hijos):
                print(f"    {idx}. {hijo}")
            el = input("Selecciona un objeto (número): ")
            if el.isdigit():
                hijos[int(el)].entrar(personaje)
        else:
            print("No hay objetos en la sala.")

    elif eleccion.lower() == "i":
        if personaje.mochila.children:
            for idx, obj in enumerate(personaje.mochila.children):
                print(f"    {idx}. {obj}")
            el = input("Selecciona un objeto (número): ")
            if el.isdigit():
                coms = personaje.mochila.children[int(el)].obtenerComandos(personaje)
                for idx, com in enumerate(coms):
                    print(f"    {idx}. {com}")
                ele = input("Selecciona un comando (número): ")
                if ele.isdigit():
                    coms[int(ele)].ejecutar(personaje)
        else:
            print("No hay objetos en la mochila.")

    elif eleccion.lower() == "c":
        coms = personaje.obtenerComandos(personaje)
        for idx, com in enumerate(coms):
            print(f"    {idx}. {com}")
        el = input("Selecciona un comando (número): ")
        if el.isdigit():
            coms[int(el)].ejecutar(personaje)