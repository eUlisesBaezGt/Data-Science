import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # NavigationToolbar2Tk)
# from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
# import matplotlib.pyplot as plt
import numpy as np
# import math
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import json
import os
from math import *


def prSetTxt(pTxt, pVal):
    pTxt.delete(0, len(pTxt.get()))
    pTxt.insert(0, pVal)


class PlotWin:

    def window(self):
        self.window = tkinter.Tk()
        self.window.title("Gráfica")
        self.window.geometry("465x250+100+200")

        self.lbl01 = tkinter.Label(self.window, text="Z =")
        self.lbl01.place(x=10, y=10)

        self.lbl02 = tkinter.Label(self.window, text="step = ")
        self.lbl02.place(x=10, y=50)

        self.lbl03 = tkinter.Label(self.window, text="Ri = ")
        self.lbl03.place(x=10, y=90)

        self.lbl04 = tkinter.Label(self.window, text="Rf = ")
        self.lbl04.place(x=10, y=130)

        self.txt01 = tkinter.Entry(self.window, width=30)
        self.txt01.place(x=50, y=10)
        prSetTxt(self.txt01, "sin(cos(0.33*X)) + cos(sin(0.55*Y))")

        self.sbLog = tkinter.Scrollbar(self.window)
        self.sbLog.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.txtLog = tkinter.Text(self.window, bg="lightgray", width=60, height=5,
                                   wrap=tkinter.NONE, yscrollcommand=self.sbLog.set)
        self.txtLog.place(x=0, y=155)
        self.sbLog.config(command=self.txtLog.yview)

        self.txt02 = tkinter.Entry(self.window, width=30)
        self.txt02.place(x=50, y=50)
        prSetTxt(self.txt02, "0.25")

        self.txt03 = tkinter.Entry(self.window, width=30)
        self.txt03.place(x=50, y=90)
        prSetTxt(self.txt03, "-5")

        self.txt04 = tkinter.Entry(self.window, width=30)
        self.txt04.place(x=50, y=130)
        prSetTxt(self.txt04, "5")

        self.btn01 = tkinter.Button(self.window, text="Mostrar", command=self.btn01_click)
        self.btn01.place(x=340, y=10, width=75)

        self.window.mainloop()

    def showPlot(self, pFunc, ri, rf, s):
        # XVec = np.arange(-5,5,0.25)
        XVec = np.arange(float(ri), float(rf), float(s))
        XSize = XVec.size
        YVec = np.arange(float(ri), float(rf), float(s))
        YSize = YVec.size
        ######print(ri, rf, s)
        ZMat = np.zeros((XSize, YSize))

        for XIdx in range(0, XSize):
            for YIdx in range(0, YSize):
                X = XVec[XIdx]
                Y = YVec[YIdx]
                Z = eval(pFunc)
                # print(X, Y, Z)
                ZMat[XIdx, YIdx] = Z
        # Zmat

        XVecG, YVecG = np.meshgrid(XVec, YVec)

        lFig = Figure(figsize=(5, 4), dpi=100)  # espacio para pintar
        lAxis = Axes3D(lFig)  # cuántos renglones y columnas, ahora es gráfica grande. renglón, columna, profundidad
        lAxis.plot_surface(XVecG, YVecG, ZMat, rstride=1, cstride=1, cmap=cm.coolwarm)

        lWin = tkinter.Tk()
        lWin.title(pFunc)
        canvas = FigureCanvasTkAgg(lFig, master=lWin)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)  # lAxis.plot(Xs,Ys, color="red")

        # lplane.show()

    def btn01_click(self):
        msg = str(self.txt01.get()) + ' \nri: ' + str(self.txt03.get()) + ' \nrf: ' + str(
            self.txt04.get()) + "\nstep: " + str(self.txt02.get()) + "\n\n"
        lDatos = list()
        lDatos.append(msg)
        lDatosJS = json.dumps(lDatos)
        Path = "/Users/saramiranda/Documents/PO/2doparcial/hola.txt"
        lFile = open(Path, "at")
        if os.path.isfile(Path):
            lNFile = open(Path, "rt")
            lNFile.close()
        self.txtLog.insert(tkinter.END, msg)
        lFile.write(lDatosJS)
        lFile.close()
        self.showPlot(self.txt01.get(), self.txt03.get(), self.txt04.get(), self.txt02.get())


myplotwin = PlotWin()
myplotwin.window()