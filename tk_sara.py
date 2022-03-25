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
    pTxt.insert(0,pVal)
#prSetTxt

class PlotWin:
    
    def window(self):
        self.window = tk.Tk()
        self.window.title("Grafica_3D")
        self.window.geometry("800x600")
        
        self.lbl01 = tk.Label(self.window, text="Z =")
        self.lbl01.place(x=10,y=10 )
        
        self.lbl02 = tk.Label(self.window, text="step = ")
        self.lbl02.place(x=10,y=50 )
        
        self.lbl03 = tk.Label(self.window, text="Ri = ")
        self.lbl03.place(x=10,y=90 )
        
        self.lbl04 = tk.Label(self.window, text="Rf = ")
        self.lbl04.place(x=10,y=130 )
        
        self.txt01 = tk.Entry(self.window , width=30)
        self.txt01.place(x=50, y=10)
        prSetTxt(self.txt01, "sin(cos(0.33*X)) + cos(sin(0.55*Y))")
        
        self.sbLog = tk.Scrollbar(self.window)
        self.sbLog.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.txtLog = tk.Text(self.window, bg="lightgray", width=60, height=5,
                                   wrap=tk.NONE, yscrollcommand=self.sbLog.set)
        self.txtLog.place(x=0, y=155)
        self.sbLog.config(command=self.txtLog.yview)
        
        
        
        
        
        