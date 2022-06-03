import random
import tkinter
import pygame

pygame.mixer.init()


def play_music():
    pygame.mixer.music.load("imperial.mp3")
    pygame.mixer.music.play(loops=0)


def carga_cartas(fotos):
    deck_s = ["♥", "♣", "♦", "♠"]
    extras = ["J", "Q", "K"]
    ext = "png"

    for symbol in deck_s:
        for carta in range(1, 11):
            img = tkinter.PhotoImage(file="Fotos/{}-{}.{}".format(str(carta), symbol, ext))
            fotos.append((carta, img))
        for carta in extras:
            img = tkinter.PhotoImage(file="Fotos/{}-{}.{}".format(str(carta), symbol, ext))
            fotos.append((10, img))


def quita_pon(frm):
    carta = deck.pop(0)
    deck.append(carta)
    tkinter.Label(frm, image=carta[1]).pack(side='left')
    return carta


def puntua(mano):
    total = 0
    a = False
    for carta in mano:
        carta_act = carta[0]
        if carta_act == 1 and not a:
            a = True
            carta_act = 11
        total += carta_act
        if total > 21 and a:
            total -= 10
            a = False
    return total


def casa_check():
    casa_tot = puntua(mano_casa)
    while 0 < casa_tot < 17:
        mano_casa.append(quita_pon(carta_casa_frm))
        casa_tot = puntua(mano_casa)
        casa_tot_label.set(casa_tot)

    jug_total = puntua(jug_mano)
    if jug_total > 21:
        res.set("¡Perdiste!")
    elif casa_tot > 21 or casa_tot < jug_total:
        res.set("¡Ganaste!")
    elif casa_tot > jug_total:
        res.set("¡La casa gana!")
    else:
        res.set("¡Empataste!")


def jug_check():
    jug_mano.append(quita_pon(jug_carta_frm))
    jug_total = puntua(jug_mano)
    jug_total_label.set(jug_total)
    if jug_total > 21:
        res.set("¡Perdiste!")


def inicio():
    jug_check()
    mano_casa.append(quita_pon(carta_casa_frm))
    casa_tot_label.set(puntua(mano_casa))
    jug_check()


def comenzar():
    global carta_casa_frm
    global jug_carta_frm
    global mano_casa
    global jug_mano

    carta_casa_frm.destroy()
    carta_casa_frm = tkinter.Frame(carta_frm, bg="#01E9FD")
    carta_casa_frm.grid(row=0, column=1, sticky='ew', rowspan=2)

    jug_carta_frm.destroy()
    jug_carta_frm = tkinter.Frame(carta_frm, bg="#01E9FD")
    jug_carta_frm.grid(row=2, column=1, sticky='ew', rowspan=2)

    res.set("")

    mano_casa = []
    jug_mano = []
    inicio()


def barajear():
    random.shuffle(deck)


def juego():
    play_music()
    inicio()
    root.mainloop()


def exit():
    pygame.mixer.music.stop()
    root.destroy()
    print("Blackjack finalizado")


root = tkinter.Tk()
root.title("KA - Blackjack def otra galaxia")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.configure(bg="#01E9FD")

root.columnconfigure(0, weight=2)
root.columnconfigure(1, weight=2)
root.columnconfigure(2, weight=2)
root.columnconfigure(3, weight=0)
root.columnconfigure(4, weight=5)
root.columnconfigure(5, weight=0)

res = tkinter.StringVar()
result = tkinter.Label(root, textvariable=res)
result.configure(bg="#01E9FD", font=("Arial", 50))
result.grid(row=0, column=0, columnspan=3)

carta_frm = tkinter.Frame(root, borderwidth=1, bg="black")
carta_frm.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

casa_tot_label = tkinter.IntVar()
tkinter.Label(carta_frm, text="Croupier", bg="black", fg="white", font=("Arial", 40)).grid(row=0, column=0)
tkinter.Label(carta_frm, textvariable=casa_tot_label, bg="black", fg="white", font=("Arial", 40)).grid(row=1, column=0)
carta_casa_frm = tkinter.Frame(carta_frm, bg="black")
carta_casa_frm.grid(row=0, column=1, sticky='ew', rowspan=2)

jug_total_label = tkinter.IntVar()
tkinter.Label(carta_frm, text="Jugador", bg="black", fg="white", font=("Arial", 40)).grid(row=2, column=0)
tkinter.Label(carta_frm, textvariable=jug_total_label, bg="black", fg="white", font=("Arial", 40)).grid(row=3, column=0)
jug_carta_frm = tkinter.Frame(carta_frm, bg="black")
jug_carta_frm.grid(row=2, column=1, sticky='ew', rowspan=2)

button_frame = tkinter.Frame(root)
button_frame.grid(row=3, column=1, columnspan=3, sticky='w')

pedir_button = tkinter.Button(button_frame, text="Pedir otra carta", command=jug_check, padx=8, width=30, height=5,
                              bg="blue", fg="white", font=("Arial", 16))
pedir_button.grid(row=0, column=0)

quedar_button = tkinter.Button(button_frame, text="Quedarse", command=casa_check, padx=5, width=30, height=5,
                               bg="green", fg="white", font=("Arial", 16))
quedar_button.grid(row=0, column=1)

reinicia_button = tkinter.Button(button_frame, text="Comenzar de nuevo", command=comenzar, width=30, height=5,
                                 bg="yellow",
                                 fg="black", font=("Arial", 16))
reinicia_button.grid(row=0, column=2)

barajear_button = tkinter.Button(button_frame, text="Barajear", command=barajear, padx=2, width=30, height=5,
                                 bg="purple", fg="white", font=("Arial", 16))
barajear_button.grid(row=0, column=3)

salir_button = tkinter.Button(button_frame, text="Salir", command=exit, padx=2, width=30, height=5, bg="red",
                              fg="white", font=("Arial", 16))
salir_button.grid(row=0, column=4)

cartas = []
carga_cartas(cartas)

deck = list(cartas) + list(cartas)
barajear()

mano_casa = []
jug_mano = []
