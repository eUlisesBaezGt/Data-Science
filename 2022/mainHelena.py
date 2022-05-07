import tkinter as tk
import matplotlib as mpl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import numpy as np

from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import json
import os

from math import *

def prSetTxt(pTxt, pVal):
    pTxt.delete(0, len(pTxt.get()))
    pTxt.insert(0, pVal)

class PlotWin:

    def window(self):
        self.window = tk.Tk()
        self.window.title("GraphsKikin")
        self.window.geometry("800x600")

        self.lbl1 = tk.Label(self.window, text = "Z = ")
        self.lbl1.place(x = 10, y = 10)

        self.lbl2 = tk.Label(self.window, text="step = ")
        self.lbl2.place(x=10, y=50)

        self.lbl3 = tk.Label(self.window, text="Ri = ")
        self.lbl3.place(x=10, y=90)

        self.txt1 = tk.Entry(self.window, width=35)
        self.txt1.place(x=50, y= 10)
        prSetTxt(self.txt1, "sin(cos(x*0.33))", "cos(sin(y*0.55))")

        self.sbLog = tk.Scrollbar(self.window)
        self.sbLog.pack(side= tk.RIGHT, fill=tk.Y)

        self.txtLog = tk.Text(self.window, bg="lightblue", width=60, height=5, wrap=tk.NONE, yscrollcommand=self.sbLog.set)
        self.txtLog.place(x=0, y=155)

        self.txtLog.place(x=0, y=155)
        self.sbLog.config(command=self.txtLog.yview)