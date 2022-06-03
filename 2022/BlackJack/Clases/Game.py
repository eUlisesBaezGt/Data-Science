import time
import random

from termcolor import colored
from Clases.Jugador import *
from Clases.Baraja import *


def print_win():
    print(colored('GANASTE', 'green'))


def print_loose():
    print(colored('PERDISTE', 'red'))


def print_tie():
    print(colored('EMPATE', 'blue'))


def add_card(baraja, player):
    if len(baraja.decks) > 15:
        pedir_carta(baraja, player)
    else:
        pass


def check_points(baraja, house, player_one, apuesta, countplayer_one, count_house):
    runcheck_points = True
    blackjack = False
    loose = False
    loose_h = False

    if len(baraja.decks) <= 15:
        runcheck_points = False

    while runcheck_points is True:
        if countplayer_one == 21:
            blackjack = True
            runcheck_points = False
        elif countplayer_one > 21:
            print_loose()
            runcheck_points = False
        else:
            print("La carta de la casa es: ", house.mano[0])
            print("Tus cartas son: ", player_one.mano)
            print("¿Quieres pedir otra carta?")
            print("1) Si")
            print("2) No")
            player_option = int(input())

            if player_option == 1:
                add_card(baraja, player_one)
                countplayer_one = check_value(player_one.mano)
                if countplayer_one > 21:
                    loose = True
                    runcheck_points = False
            else:
                for i in range(5):
                    if count_house < 17:
                        add_card(baraja, house)
                        count_house = check_value(house.mano)
                        if count_house > 21:
                            loose_h = True
                    else:
                        runcheck_points = False

    print("Mano jugador: ", player_one.mano, " = ", countplayer_one, " pts")
    print("Mano casa: ", house.mano, " = ", count_house, " pts")

    if blackjack:
        print_win()
        player_one.ganadas += 1
        player_one.money += apuesta
        player_one.detalles()

    elif loose_h:
        print_win()
        player_one.ganadas += 1
        player_one.detalles()
    else:
        if not loose:
            if countplayer_one > count_house:
                print_win()
                player_one.ganadas += 1
                player_one.detalles()

            elif countplayer_one < count_house:
                print_loose()
                player_one.perdidas += 1
                player_one.money -= apuesta
                player_one.detalles()
            else:
                print_tie()
                player_one.empates += 1
                player_one.detalles()
        else:
            print_loose()
            player_one.perdidas += 1
            player_one.money -= apuesta
            player_one.detalles()

    time.sleep(3)
    print("Cartas restantes: ", len(baraja.decks))


def start_game(baraja, player_one, house):
    apuesta = player_one.apostar()
    player_one.mano = []
    house.mano = []

    if len(baraja.decks) > 15:
        for i in range(4):
            if i < 2:
                random_card = random.choice(baraja.decks)
                house.mano.append(random_card)

                for e in range(len(baraja.decks)):
                    if baraja.decks[e] == random_card:
                        baraja.decks.pop(e)
                        break
            else:
                random_card = random.choice(baraja.decks)
                player_one.mano.append(random_card)

                for e in range(len(baraja.decks)):
                    if baraja.decks[e] == random_card:
                        baraja.decks.pop(e)
                        break

        count_house = check_value(house.mano)
        countplayer_one = check_value(player_one.mano)

        check_points(baraja, house, player_one, apuesta, countplayer_one, count_house)

    else:
        pass
