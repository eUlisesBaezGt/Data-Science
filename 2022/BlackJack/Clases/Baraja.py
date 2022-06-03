import numpy as np


def pedir_carta(baraja, player):
    if len(baraja.decks) > 15:
        card = baraja.decks[-1]
        baraja.decks.pop()
        player.mano.append(card)
    else:
        pass


class Baraja:
    hearts = ["♥A", "♥2", "♥3", "♥4", "♥5", "♥6", "♥7", "♥8", "♥9", "♥10", "♥jack", "♥queen", "♥king"]
    clubs = ["♣A", "♣2", "♣3", "♣4", "♣5", "♣6", "♣7", "♣8", "♣9", "♣10", "♣jack", "♣queen", "♣king"]
    diamonds = ["♦A", "♦2", "♦3", "♦4", "♦5", "♦6", "♦7", "♦8", "♦9", "♦10", "♦jack", "♦queen", "♦king"]
    spades = ["♠A", "♠2", "♠3", "♠4", "♠5", "♠6", "♠7", "♠8", "♠9", "♠10", "♠jack", "♠queen", "♠king"]

    deck = [hearts, clubs, diamonds, spades]
    decks = []

    def numdecks(self):
        print("Elija el número de barajas para jugar\n")
        print("1 Baraja")
        print("2 Barajas")
        print("3 Barajas")
        print("4 Barajas")
        print("5 Barajas")
        print("6 Barajas")
        print("7 Barajas")
        print("8 Barajas")
        option = int(input("Opción: "))

        for n in range(option):
            for i in range(4):
                for j in range(13):
                    self.decks.append(self.deck[i][j])

    def barajear(self):
        np.random.shuffle(self.decks)
