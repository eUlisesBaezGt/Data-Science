def validar_nombre():
    run_name = True
    while run_name is True:
        n = input("Ingrese su nombre: ")
        if len(n) < 3:
            print("El nombre es muy corto")
        else:
            return n


def validar_monto_inicial():
    run_monto = True
    while run_monto is True:
        n = input("Ingrese el monto inicial: ")
        if n.isdigit():
            n = float(n)
            return n
        else:
            print("Monto inválido")


def validar_monto_apuesta():
    run_apuesta = True
    while run_apuesta is True:
        n = input("Ingrese el monto a apostar: ")
        if n.isdigit():
            n = float(n)
            return n
        else:
            print("Monto inválido")


def validar_monto_fichas():
    run_fichas = True
    while run_fichas is True:
        print("Cada ficha equivale a $100")
        fichas = input("Ingrese el número de fichas a depositar: ")
        if fichas.isdigit():
            fichas = int(fichas)
            money = fichas * 100
            return money
        else:
            print("Número inválido")


def check_value(cards):
    count = 0
    for i in range(len(cards)):
        if "2" in cards[i]:
            count += 2
        elif "3" in cards[i]:
            count += 3
        elif "4" in cards[i]:
            count += 4
        elif "5" in cards[i]:
            count += 5
        elif "6" in cards[i]:
            count += 6
        elif "7" in cards[i]:
            count += 7
        elif "8" in cards[i]:
            count += 8
        elif "9" in cards[i]:
            count += 9
        elif "10" in cards[i]:
            count += 10
        elif "jack" in cards[i]:
            count += 10
        elif "queen" in cards[i]:
            count += 10
        elif "king" in cards[i]:
            count += 10
        elif "A" in cards[i]:
            if count >= 11:
                count += 1
            else:
                count += 11
    return count


class Jugador:

    def __init__(self, name, money):
        self.nombre = name
        self.money = money
        self.ganadas = 0
        self.perdidas = 0
        self.empates = 0

    def detalles(self):
        print("-----------------------------")
        print("Monto restante: ", self.money)
        print("-----------------------------")

    def detallesfinal(self):
        print("-----------------------------")
        print("Nombre: ", self.nombre)
        print("Monto restante: ", self.money)
        print("Partidas ganadas: ", self.ganadas)
        print("Partidas perdidas: ", self.perdidas)
        print("Partidas empatadas: ", self.empates)
        print("Porcentaje de victorias: ", (self.ganadas / (self.ganadas + self.perdidas + self.empates)) * 100)
        print("-----------------------------")

    def apostar(self):
        apuesta = validar_monto_apuesta()
        while apuesta > self.money:
            print("No puede apostar más de lo que tiene")
            f = input("¿Desea depositar fichas? (S/N): ")
            if f == "S":
                self.depositar_fichas()
                self.apostar()
            elif f == "N":
                self.apostar()
            else:
                print("Opcion invalida")
                self.apostar()
        print("Apuesta realizada")
        return apuesta

    def depositar_fichas(self):
        deposito = validar_monto_fichas()
        self.money += deposito
        print("Deposito de fichas realizado")