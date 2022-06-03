from Clases.Game import start_game


def ask_round(baraja, jugador, croupier):
    if len(baraja.decks) > 15:
        respuesta = input("¿Quiere seguir jugando? (S/N): ")
        if respuesta == "S":
            start_game(baraja, jugador, croupier)
        elif respuesta == "N":
            jugador.detallesfinal()
            print("Regresando al menu principal.............\n--------------------------------\n")
        else:
            print("Respuesta no valida, intente de nuevo")

    else:
        print("No hay mas cartas, regresando al menu principal")
        print("--------------------------------\n")


def nuevo_juego(baraja, jugador, croupier):
    if len(baraja.decks) > 15:
        start_game(baraja, jugador, croupier)
        ask_round(baraja, jugador, croupier)
    else:
        return


def jugar(baraja, jugador, croupier):
    juego = True
    partidas = 0
    while juego is True:
        if partidas == 0:
            if len(baraja.decks) > 15:
                respuesta = input("¿Quiere comenzar a jugar? (S/N): ")
                if respuesta == "S":
                    partidas = 1
                    print("Juego iniciado\n")
                    nuevo_juego(baraja, jugador, croupier)
                if len(baraja.decks) <= 15:
                    print("Juego terminado\n")
                    juego = False
                elif respuesta == "N":
                    print("Regresando al menu principal....\n--------------------------------\n")
                    juego = False

        else:
            if len(baraja.decks) <= 15:
                print("Juego terminado\n")
                juego = False
            else:
                respuesta = input("¿Quiere seguir jugando? (S/N): ")
                if respuesta == "S":
                    if len(baraja.decks) <= 15:
                        print("Juego terminado\n")
                        juego = False
                    else:
                        nuevo_juego(baraja, jugador, croupier)
                elif respuesta == "N":
                    jugador.detallesfinal()
                    print("Regresando al menu principal....\n--------------------------------\n")
                    juego = False
