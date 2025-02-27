from creator import Creator, CreatorB
from juegoLaberinto import Juego


FM = Creator()
juego = Juego()
juego.laberinto = juego.crear_laberinto_2_hab_FM(FM)
hab1=juego.obtener_habitacion(1)
hab2=juego.obtener_habitacion(2)
print(hab1.num)
print(hab2.num)

#laberinto con paredes bomba
FMb = CreatorB()
juego.laberinto = juego.crear_laberinto_2_hab_FM(FMb)
hab1=juego.obtener_habitacion(1)
hab2=juego.obtener_habitacion(2)
print(hab1.norte.activa)
print(hab2.sur.activa)


# Crear laberinto de 4 habitaciones
FM = Creator()
juego.laberinto = juego.crear_laberinto_4_hab(FM)



# Mostrar el número de cada habitación
for habitacion in juego.laberinto.habitaciones:
    print(f"Habitación {habitacion.num}")
    if hasattr(habitacion, 'bicho'):
        bicho = habitacion.bicho





from creator import Creator, CreatorB
from juegoLaberinto import Juego, Bomba


#ejemplo de uso
FM = Creator()
juego = Juego()
juego.laberinto = juego.crear_laberinto_2_hab_FM(FM)
hab1=juego.obtener_habitacion(1)
hab2=juego.obtener_habitacion(2)
print(hab1.num)
print(hab2.num)




#laberinto con paredes bomba
FMb = CreatorB()
juego.laberinto = juego.crear_laberinto_2_hab_FM(FMb)
hab1=juego.obtener_habitacion(1)
hab2=juego.obtener_habitacion(2)
print(hab1.norte.activa)
print(hab2.sur.activa)

# Crear laberinto de 4 habitaciones
FM = Creator()
juego.laberinto = juego.crear_laberinto_4_hab(FM)

# Mostrar el número de cada habitación
for habitacion in juego.laberinto.habitaciones:
    print(f"Habitación {habitacion.num}")
    if hasattr(habitacion, 'bicho'):
        bicho = habitacion.bicho





from creator import Creator, CreatorB
from juegoLaberinto import Juego, Bomba


#ejemplo de uso
FM = Creator()
juego = Juego()
juego.laberinto = juego.crear_laberinto_2_hab_FM(FM)
hab1=juego.obtener_habitacion(1)
hab2=juego.obtener_habitacion(2)
print(hab1.num)
print(hab2.num)




#laberinto con paredes bomba
FMb = CreatorB()
juego.laberinto = juego.crear_laberinto_2_hab_FM(FMb)
hab1=juego.obtener_habitacion(1)
hab2=juego.obtener_habitacion(2)
print(hab1.norte.activa)
print(hab2.sur.activa)

# Crear laberinto de 4 habitaciones
FM = Creator()
juego.laberinto = juego.crear_laberinto_4_hab(FM)

# Mostrar el número de cada habitación
for habitacion in juego.laberinto.habitaciones:
    print(f"Habitación {habitacion.num}")
    if hasattr(habitacion, 'bicho'):
        bicho = habitacion.bicho



from creator import Creator, CreatorB
from juegoLaberinto import Juego, Bomba




#ejemplo de uso
fm = Creator()
juego = Juego()
juego.laberinto = juego.crear_laberinto_2_hab_FM(fm)
hab1=juego.obtener_habitacion(1)
hab2=juego.obtener_habitacion(2)
print(hab1.num)
print(hab2.num)




#laberinto con paredes bomba
FMb = CreatorB()
juego.laberinto = juego.crear_laberinto_2_hab_FM(FMb)
hab1=juego.obtener_habitacion(1)
hab2=juego.obtener_habitacion(2)
print(hab1.norte.activa)
print(hab2.sur.activa)




# Crear laberinto de 4 habitaciones
FM = Creator()
juego.laberinto = juego.crear_laberinto_4_hab(FM)

# Mostrar el número de cada habitación
for habitacion in juego.laberinto.habitaciones:
    print(f"Habitación {habitacion.num}")
    if hasattr(habitacion, 'bicho'):
        bicho = habitacion.bicho






from creator import Creator, CreatorB
from juegoLaberinto import Juego, Bomba


#ejemplo de uso
fm = Creator()
juego = Juego()
juego.laberinto = juego.crear_laberinto_2_hab_FM(fm)
hab1=juego.obtener_habitacion(1)
hab2=juego.obtener_habitacion(2)
print(hab1.num)
print(hab2.num)

#laberinto con paredes bomba
FMb = CreatorB()
juego.laberinto = juego.crear_laberinto_2_hab_FM(FMb)
hab1=juego.obtener_habitacion(1)
hab2=juego.obtener_habitacion(2)
print(hab1.norte.activa)
print(hab2.sur.activa)




# Crear laberinto de 4 habitaciones
FM = Creator()
juego.laberinto = juego.crear_laberinto_4_hab(FM)

# Mostrar el número de cada habitación
for habitacion in juego.laberinto.habitaciones:
    print(f"Habitación {habitacion.num}")
    if hasattr(habitacion, 'bicho'):
        bicho = habitacion.bicho









from creator import Creator, CreatorB
from juegoLaberinto import Juego, Bomba



#ejemplo de uso
FM = Creator()
juego = Juego()
juego.laberinto = juego.crear_laberinto_2_hab_FM(FM)
hab1=juego.obtener_habitacion(1)
hab2=juego.obtener_habitacion(2)
print(hab1.num)
print(hab2.num)

#laberinto con paredes bomba
FMb = CreatorB()
juego.laberinto = juego.crear_laberinto_2_hab_FM(FMb)
hab1=juego.obtener_habitacion(1)
hab2=juego.obtener_habitacion(2)
print(hab1.norte.activa)
print(hab2.sur.activa)




# Crear laberinto de 4 habitaciones
FM = Creator()
juego.laberinto = juego.crear_laberinto_4_hab(FM)

# Mostrar el número de cada habitación
for habitacion in juego.laberinto.habitaciones:
    print(f"Habitación {habitacion.num}")
    if hasattr(habitacion, 'bicho'):
        bicho = habitacion.bicho
        print(f"  Bicho: Vidas={bicho.vidas}, Poder={bicho.poder}, Posicion={bicho.posicion.num}")

# Crear laberinto de 2 habitaciones con bombas (Habitación 1 al este, Habitación 2 al oeste)
FM = Creator()
juego2 = Juego()
juego2.laberinto = juego2.crear_laberinto_2_hab_bomba(FM)
hab1 = juego2.obtener_habitacion(1)
hab2 = juego2.obtener_habitacion(2)

print("\nLaberinto de 2 habitaciones con bombas:")
print(f"Habitación 1 tiene bomba al este: {hasattr(hab1, 'este') and hasattr(hab1.este, 'esBomba') and hab1.este.esBomba()}")
print(f"Habitación 2 tiene bomba al oeste: {hasattr(hab2, 'oeste') and hasattr(hab2.oeste, 'esBomba') and hab2.oeste.esBomba()}")
