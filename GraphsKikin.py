import tkinter
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
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

    def get_log(self):
        n = 0
        if os.path.isfile(self.path):
            read_file = open(self.path, "r")

            if os.stat(self.path).st_size != 0:

                for line in read_file:

                    id = "#: " + str(n)
                    n += 1
                    self.log.insert(tkinter.END, id)
                    self.log.insert(tkinter.END, "\n")
                    line = json.loads(line)

                    for i in range(4):

                        self.log.insert(tkinter.END, line[1][i][0])
                        self.log.insert(tkinter.END, str(line[1][i][1]))
                        self.log.insert(tkinter.END, "\n")
                    self.log.insert(tkinter.END, "\n")

                read_file.close()

    def createWindow(self):
        self.window = tkinter.Tk()
        self.window.title("GRAPHS")
        self.window.geometry("800x600")

        self.scrlbr = tkinter.Scrollbar(self.window)
        self.scrlbr.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        self.hrz_scrlbr = tkinter.Scrollbar(self.window, orient="horizontal")
        self.hrz_scrlbr.pack(side=tkinter.BOTTOM, fill=tkinter.X)

        self.log = tkinter.Text(self.window, bg="lightblue", width=64, height=9,
                                wrap=tkinter.NONE, xscrollcommand=self.hrz_scrlbr.set, yscrollcommand=self.scrlbr.set)
        self.log.place(x=10, y=170)

        self.scrlbr.config(command=self.log.yview)

        self.lower_limit_lbl = tkinter.Label(self.window, text='Lower Limit')
        self.lower_limit_lbl.place(x=10, y=10)

        self.lw_txt = tkinter.Entry(self.window, bg="lightblue", width=50)
        self.lw_txt.place(x=75, y=10)

        self.upper_limit_lbl = tkinter.Label(self.window, text='Upper Limit')
        self.upper_limit_lbl.place(x=10, y=40)

        self.up_txt = tkinter.Entry(self.window, bg="lightblue", width=50)
        self.up_txt.place(x=75, y=40)

        self.step_lbl = tkinter.Label(self.window, text='Step')
        self.step_lbl.place(x=10, y=70)

        self.step_txt = tkinter.Entry(self.window, bg="lightblue", width=50)
        self.step_txt.place(x=75, y=70)

        self.function_lbl = tkinter.Label(self.window, text="Function")
        self.function_lbl.place(x=10, y=100)

        self.fnc_txt = tkinter.Entry(self.window, bg="lightblue", width=50)
        self.fnc_txt.place(x=75, y=100)

        self.show_btn = tkinter.Button(
            self.window, text="SHOW", command=self.show_btn_click)
        self.show_btn.place(x=600, y=130, width=75)

        self.path = "./log.txt"

        aux = -1
        all_json = ""

        if os.path.isfile(self.path):
            file = open(self.path, "r")

            if os.stat(self.path).st_size != 0:

                for line in file:

                    if (json.loads(line)[0] > aux):

                        aux = json.loads(line)[0]
                        all_json = line

                data = json.loads(all_json)
                prSetTxt(self.lw_txt, str(data[1][1][1]))
                prSetTxt(self.up_txt, str(data[1][2][1]))
                prSetTxt(self.step_txt, str(data[1][3][1]))
                prSetTxt(self.fnc_txt, data[1][0][1])

            file.close()

        self.get_log()
        self.window.mainloop()

    def showPlot(self, fnc, lw, up, stp):
        aux = -1
        if os.path.isfile(self.path):

            file = open(self.path, "r")
            if os.stat(self.path).st_size != 0:

                for line in file:

                    if (json.loads(line)[0] > aux):

                        aux = json.loads(line)[0]

        coll = [(aux+1), [["Function: ", str(fnc)], ["Lower Limit: ",
                                                     lw], ["Upper Limit: ", up], ["Step: ", stp]]]

        self.log.insert(tkinter.END, ("id: " + str(aux+1)+"\n"))

        for i in range(4):

            self.log.insert(tkinter.END, coll[1][i][0])
            self.log.insert(tkinter.END, str(coll[1][i][1]))
            self.log.insert(tkinter.END, "\n")

        self.log.insert(tkinter.END, "\n")

        all_json = json.dumps(coll)

        if os.path.isfile(self.path):
            file = open(self.path, "a")
            file.write(all_json)
            file.write("\r")
            file.close()

        xs = np.arange(lw, up, stp)
        xs_sz = xs.size
        ys = np.arange(lw, up, stp)
        ys_sz = ys.size

        zrs = np.zeros((xs_sz, ys_sz))

        for i in range(0, xs_sz):
            for j in range(0, ys_sz):
                X = xs[i]
                Y = ys[j]
                Z = eval(fnc)
                zrs[i, j] = Z

        xv, yv = np.meshgrid(xs, ys)

        fig = Figure(figsize=(10, 8), dpi=150)
        Axis = Axes3D(fig)
        Axis.plot_surface(xv, yv, zrs, rstride=1, cstride=1, cmap='plasma')

        W = tkinter.Tk()
        W.title(fnc)
        canvas = FigureCanvasTkAgg(fig, master=W)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    def show_btn_click(self):
        self.showPlot(self.fnc_txt.get(), float(self.lw_txt.get()),
                      float(self.up_txt.get()), float(self.step_txt.get()))


plot = PlotWin()
plot.createWindow()
