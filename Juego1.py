print ("Hachiko ♥")

import random

#Personajes
personajes = {
    'Caballero': (10, 5, 2), 
    'Hechicero': (10, 3, 4)}

lista_personajes = list(personajes.keys())

#Inicio del Juego 
print ("¡Bienvenido al juego! :) \n Estos son los personajes disponibles: ")

for i, nombre in enumerate(personajes, 1):
    print (i, "Personaje:", nombre, 
           "Vida:",personajes[nombre][0], 
           "Ataque:",personajes[nombre][1], 
           "Defensa:",personajes[nombre][2])

#Seleccion de los personajes
seleccion_valida = False
while not seleccion_valida:
    try:
        seleccion = int(input(" Por favor selecciona tu personaje (1 o 2): "))
        if seleccion == 1:
            personaje_jugador = "Caballero"
            print("\n¡Muy bien! Has seleccionado al Caballero")
            seleccion_valida = True

        elif seleccion == 2:
            personaje_jugador = "Hechicero" 
            print("\n¡Muy bien! Has seleccionado al Hechicero")
            seleccion_valida = True

        else:
            print("Opción inválida. Intenta de nuevo.")
    except ValueError:
        print("Error: Debes ingresar un número (1 o 2).")

#atributos del jugador
vida_jugador, ataque_jugador, defensa_jugador = personajes[personaje_jugador]

#seleccion del oponente
personaje_oponente = random.choice([p for p in lista_personajes if p != personaje_jugador])
vida_oponente, ataque_oponente, defensa_oponente = personajes[personaje_oponente]
print ("Te enfrentaras a: ",personaje_oponente)

#Combate
acciones = ["Atacar", "Defender"]

while vida_jugador > 0 and vida_oponente > 0:
    print("\n¿Qué deseas hacer?")
    for i, accion in enumerate(acciones, 1):
        print(i, accion)
    try:
        eleccion_accion = int(input("Introduce el número de tu acción: ")) - 1
        if eleccion_accion not in [0, 1]:
            print("Opción inválida. Elige 1 o 2.")
            continue
        accion_jugador = acciones[eleccion_accion]
    except ValueError:
        print("Error: Debes ingresar un número.")
        continue
    accion_oponente = random.choice(acciones)

    print(f"\n{personaje_jugador} ha elegido {accion_jugador}.")
    print(f"{personaje_oponente} ha elegido {accion_oponente}.")

    # Lógica del combate
    if accion_jugador == "Atacar" and accion_oponente == "Atacar":
        vida_jugador -= max(1, ataque_oponente - defensa_jugador)
        vida_oponente -= max(1, ataque_jugador - defensa_oponente)
    elif accion_jugador == "Atacar" and accion_oponente == "Defender":
        vida_oponente -= max(1, (ataque_jugador - defensa_oponente) // 2)
    elif accion_jugador == "Defender" and accion_oponente == "Atacar":
        vida_jugador -= max(1, (ataque_oponente - defensa_jugador) // 2)
    elif accion_jugador == "Defender" and accion_oponente == "Defender":
        print("¡Ambos se defienden! Nada ocurre.")

    print(f"\nVida restante - {personaje_jugador}: {vida_jugador}, {personaje_oponente}: {vida_oponente}")

# Determinar ganador
if vida_jugador <= 0:
    print(f"\n{personaje_jugador} ha sido derrotado. {personaje_oponente} gana la batalla.")
elif vida_oponente <= 0:
    print(f"\n{personaje_oponente} ha sido derrotado. ¡{personaje_jugador} gana la batalla!")

print("Fin del juego.")