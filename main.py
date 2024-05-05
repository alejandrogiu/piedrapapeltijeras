import random

def obtener_elecciones():
    eleccion_jugador = input("Elige una opción (piedra, papel o tijeras): ")
    opciones = ["piedra", "papel", "tijeras"]
    eleccion_computadora = random.choice(opciones)
    elecciones = {"jugador": eleccion_jugador, "computadora": eleccion_computadora}
    return elecciones

def verificar_ganador(jugador, computadora):
    print(f"Tú elegiste {jugador}, la computadora eligió {computadora}")
    if jugador == computadora:
        return "¡Es un empate!"
    elif jugador == "piedra":
        if computadora == "tijeras":
            return "¡Piedra aplasta tijeras! ¡Ganaste!"
        else:
            return "¡Papel cubre piedra! Perdiste."
    elif jugador == "papel":
        if computadora == "piedra":
            return "¡Papel cubre piedra! ¡Ganaste!"
        else:
            return "¡Tijeras cortan papel! Perdiste."
    elif jugador == "tijeras":
        if computadora == "papel":
            return "¡Tijeras cortan papel! ¡Ganaste!"
        else:
            return "¡Piedra aplasta tijeras! Perdiste."

elecciones = obtener_elecciones()
resultado = verificar_ganador(elecciones["jugador"], elecciones["computadora"])
print(resultado)
