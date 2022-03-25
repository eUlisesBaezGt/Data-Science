import tkinter
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
from math import *
import json
import os


def prSetTxt(pTxt, pVal):
    pTxt.delete(0, len(pTxt.get()))
    pTxt.insert(0, pVal)


class PlotWin:
    def _getLog(self):
        c = 0
        if os.path.isfile(self.path):
            lFile = open(self.path, "r")
            if os.stat(self.path).st_size != 0:
                for lin in lFile:
                    ind = "ind: " + str(c)
                    c += 1
                    self.txtLog.insert(tkinter.END, ind)
                    self.txtLog.insert(tkinter.END, "\n")
                    lin = json.loads(lin)
                    for i in range(4):
                        self.txtLog.insert(tkinter.END, lin[1][i][0])
                        self.txtLog.insert(tkinter.END, str(lin[1][i][1]))
                        self.txtLog.insert(tkinter.END, "\n")
                    self.txtLog.insert(tkinter.END, "\n")
                lFile.close()

    def createWindow(self):
        self.window = tkinter.Tk()

        self.window.title("Plot")
        self.window.geometry("550x350+100+200")

        self.frame = tkinter.LabelFrame(self.window, text="Historial", pady=20)
        self.frame.place(x=415, y=10)

        self.sbLog = tkinter.Scrollbar(self.window)
        self.sbLog.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.bsbLog = tkinter.Scrollbar(self.window, orient="horizontal")
        self.bsbLog.pack(side=tkinter.BOTTOM, fill=tkinter.X)
        self.txtLog = tkinter.Text(self.window, bg="lightgray", width=64, height=9,
                                   wrap=tkinter.NONE, xscrollcommand=self.bsbLog.set, yscrollcommand=self.sbLog.set)
        self.txtLog.place(x=10, y=170)
        self.sbLog.config(command=self.txtLog.yview)

        self.lblHist = tkinter.Label(self.window, text="Acceder a historial", font=('bold', 10))
        self.lblHist.place(x=415, y=10)
        self.lblInd = tkinter.Label(self.window, text="ind:")
        self.lblInd.place(x=415, y=40)
        self.txtInd = tkinter.Entry(self.window, bg="lightgray", width=10)
        self.txtInd.place(x=460, y=40)
        self.btnFnd = tkinter.Button(self.window, text="Buscar", command=self.btnFnd_click)
        self.btnFnd.place(x=460, y=65)

        self.btnClear = tkinter.Button(self.window, fg="red", text="Borrar historial", command=self.btnClear_click,
                                       width=15)
        self.btnClear.place(x=415, y=100)

        self.lblInf = tkinter.Label(self.window, text='Lim. Inf.= ')
        self.lblInf.place(x=10, y=10)
        self.txtInf = tkinter.Entry(self.window, bg="lightgray", width=50)
        self.txtInf.place(x=75, y=10)

        self.lblSup = tkinter.Label(self.window, text='Lim. Sup.= ')
        self.lblSup.place(x=10, y=40)
        self.txtSup = tkinter.Entry(self.window, bg="lightgray", width=50)
        self.txtSup.place(x=75, y=40)

        self.lblStep = tkinter.Label(self.window, text='Step= ')
        self.lblStep.place(x=10, y=70)
        self.txtStep = tkinter.Entry(self.window, bg="lightgray", width=50)
        self.txtStep.place(x=75, y=70)

        self.lbl01 = tkinter.Label(self.window, text="Z= ")
        self.lbl01.place(x=10, y=100)
        self.txt01 = tkinter.Entry(self.window, bg="lightgray", width=50)
        self.txt01.place(x=75, y=100)

        self.btn01 = tkinter.Button(self.window, text="Muestra", command=self.btn01_click)

        self.btn01.place(x=10, y=130, width=75)

        self.path = "PATH"
        idx2 = -1
        datosJson = ""

        if os.path.isfile(self.path):
            archivo = open(self.path, "r")
            if os.stat(self.path).st_size != 0:
                for linea in archivo:
                    if (json.loads(linea)[0] > idx2):
                        idx2 = json.loads(linea)[0]
                        datosJson = linea
                datos = json.loads(datosJson)
                prSetTxt(self.txtInf, str(datos[1][1][1]))
                prSetTxt(self.txtSup, str(datos[1][2][1]))
                prSetTxt(self.txtStep, str(datos[1][3][1]))
                prSetTxt(self.txt01, datos[1][0][1])
            archivo.close()

        self._getLog()
        self.window.mainloop()

    def showPlot(self, pFunc, pInf, pSup, pStep):
        idx = -1
        if os.path.isfile(self.path):
            archivo = open(self.path, "rt")
            if os.stat(self.path).st_size != 0:
                for linea in archivo:
                    if (json.loads(linea)[0] > idx):
                        idx = json.loads(linea)[0]

        lista = [(idx + 1), [["Funcion: ", str(pFunc)], ["Limite inferior: ", pInf], ["Limite superior: ", pSup],
                             ["Step: ", pStep]]]

        self.txtLog.insert(tkinter.END, ("ind: " + str(idx + 1) + "\n"))
        for i in range(4):
            self.txtLog.insert(tkinter.END, lista[1][i][0])
            self.txtLog.insert(tkinter.END, str(lista[1][i][1]))
            self.txtLog.insert(tkinter.END, "\n")
        self.txtLog.insert(tkinter.END, "\n")

        listaJson = json.dumps(lista)
        if os.path.isfile(self.path):
            archivo = open(self.path, "a")
            archivo.write(listaJson)
            archivo.write("\r")
            archivo.close()

        XVec = np.arange(pInf, pSup, pStep)
        XSize = XVec.size
        YVec = np.arange(pInf, pSup, pStep)
        YSize = YVec.size

        ZMat = np.zeros((XSize, YSize))

        for XIdx in range(0, XSize):
            for YIdx in range(0, YSize):
                X = XVec[XIdx]
                Y = YVec[YIdx]
                Z = eval(pFunc)
                ZMat[XIdx, YIdx] = Z

        XVecG, YVecG = np.meshgrid(XVec, YVec)

        lFig = Figure(figsize=(5, 4), dpi=100)  # espacio para pintar
        lAxis = Axes3D(lFig)  # cuántos renglones y columnas, ahora es gráfica grande. renglón, columna, profundidad
        lAxis.plot_surface(XVecG, YVecG, ZMat, rstride=1, cstride=1, cmap='plasma')

        lWin = tkinter.Tk()
        lWin.title(pFunc)
        canvas = FigureCanvasTkAgg(lFig, master=lWin)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        # lPlane.show()

    # showPlot. pinta en un archivo gráfico

    def btn01_click(self):
        self.showPlot(self.txt01.get(), float(self.txtInf.get()), float(self.txtSup.get()), float(self.txtStep.get()))

    def btnFnd_click(self):
        ind = int(self.txtInd.get())
        found = False
        if os.path.isfile(self.path):
            archivo = open(self.path, "rt")
            for linea in archivo:
                lin = json.loads(linea)
                if (lin[0] == ind):
                    self.showPlot(lin[1][0][1], lin[1][1][1], lin[1][2][1], lin[1][3][1])
                    prSetTxt(self.txtInf, str(lin[1][1][1]))
                    prSetTxt(self.txtSup, str(lin[1][2][1]))
                    prSetTxt(self.txtStep, str(lin[1][3][1]))
                    prSetTxt(self.txt01, lin[1][0][1])
        if found == False:
            self.txtLog.insert(tkinter.END, "No se encro esa operacion")
            self.txtLog.insert(tkinter.END, "\n")

    def btnClear_click(self):
        if os.path.isfile(self.path):
            archivo = open(self.path, "wt")
            archivo.write("")
        self.txtLog.delete('1.0', tkinter.END)
    # btn01_click


# PlotWin

myPlotWin = PlotWin()
myPlotWin.createWindow()


#%%
