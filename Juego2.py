import random

class Personaje:
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
    
    def atacar(self, oponente):
        daño = max(1, self.ataque - oponente.defensa)
        oponente.vida -= daño
        print(f"{self.nombre} ataca a {oponente.nombre} y causa {daño} de daño.")
    
    def defender(self):
        print(f"{self.nombre} se defiende, reduciendo el daño recibido.")

class Caballero(Personaje):
    def __init__(self):
        super().__init__("Caballero", 10, 5, 2)

class Hechicero(Personaje):
    def __init__(self):
        super().__init__("Hechicero", 10, 3, 4)

# Inicio del juego
print("¡Bienvenido al juego! :) \nEstos son los personajes disponibles:")

opciones_personajes = [Caballero(), Hechicero()]
for i, personaje in enumerate(opciones_personajes, 1):
    print(f"{i}. {personaje.nombre} - Vida: {personaje.vida}, Ataque: {personaje.ataque}, Defensa: {personaje.defensa}")

# Selección del jugador
seleccion_valida = False
while not seleccion_valida:
    try:
        seleccion = int(input("Por favor selecciona tu personaje (1 o 2): "))
        if seleccion in [1, 2]:
            personaje_jugador = opciones_personajes[seleccion - 1]
            print(f"\n¡Muy bien! Has seleccionado a {personaje_jugador.nombre}")
            seleccion_valida = True
        else:
            print("Opción inválida. Intenta de nuevo.")
    except ValueError:
        print("Error: Debes ingresar un número (1 o 2).")

# Selección del oponente
personaje_oponente = random.choice([p for p in opciones_personajes if p.nombre != personaje_jugador.nombre])
print(f"Te enfrentarás a: {personaje_oponente.nombre}")

# Combate
acciones = ["Atacar", "Defender"]
while personaje_jugador.vida > 0 and personaje_oponente.vida > 0:
    print("\n¿Qué deseas hacer?")
    for i, accion in enumerate(acciones, 1):
        print(f"{i}. {accion}")
    
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

    print(f"\n{personaje_jugador.nombre} ha elegido {accion_jugador}.")
    print(f"{personaje_oponente.nombre} ha elegido {accion_oponente}.")

    if accion_jugador == "Atacar":
        personaje_jugador.atacar(personaje_oponente)
    else:
        personaje_jugador.defender()
    
    if accion_oponente == "Atacar":
        personaje_oponente.atacar(personaje_jugador)
    else:
        personaje_oponente.defender()

    print(f"\nVida restante - {personaje_jugador.nombre}: {personaje_jugador.vida}, {personaje_oponente.nombre}: {personaje_oponente.vida}")

#Ganador
if personaje_jugador.vida <= 0:
    print(f"\n{personaje_jugador.nombre} ha sido derrotado. {personaje_oponente.nombre} gana la batalla.")
elif personaje_oponente.vida <= 0:
    print(f"\n{personaje_oponente.nombre} ha sido derrotado. ¡{personaje_jugador.nombre} gana la batalla!")

print("Fin del juego.")
