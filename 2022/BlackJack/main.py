from Clases.Jugador import *
from Clases.Jugar import *
from Clases.Baraja import *
import time
import os


def clear_console():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear_console')


runGame = True
band = False

print("♠ ♥ ♣ ♦ ♠ ♥ ♣ ♦ ♠ ♥ ♣ ♦ ♠ ♥ ♣ ♦ BIENVENIDO A BLACKJACK ♠ ♥ ♣ ♦ ♠ ♥ ♣ ♦ ♠ ♥ ♣ ♦ ♠ ♥ ♣ ♦")
print("\nCaptura de datos")
print("------------------------------")
b = Baraja()
name = validar_nombre()
money = validar_monto_inicial()
p = Jugador(name, money)
h = Jugador("Croupier", 1000000)

while runGame is True:

    print("\nMENU PRINCIPAL")
    print("-------------------\n")
    print("1) Elegir el número de barajas para juego")
    print("2) Jugar solo contra la casa")
    print("3) Salir")
    op = int(input("Seleccione una opción: "))
    time.sleep(3)
    clear_console()

    if op == 1:
        b.numdecks()
        b.barajear()
        band = True

    elif op == 2:
        if band is True:
            jugar(b, p, h)
            p.detalles()
        else:
            print("No ha elegido el número de barajas")
            print("Por favor, vuelva a intentarlo")
            print("\n")
            continue
    elif op == 3:
        runGame = False
        print("Gracias por jugar con nosotros")
        print("♠ ♥ ♣ ♦ ♠ ♥ ♣ ♦ ♠ ♥ ♣ ♦ ♠ ♥ ♣ ♦ SALIENDO DE BLACKJACK ♠ ♥ ♣ ♦ ♠ ♥ ♣ ♦ ♠ ♥ ♣ ♦ ♠ ♥ ♣ ♦")
        print("------------------------------")

    else:
        print("Opción inválida")
        print("Por favor, vuelva a intentarlo")
        print("\n")
        continue
