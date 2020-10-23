# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 05:47:15 2020

@author: navee
"""

from Mortgage import Mortgage
from Calculator import Calculator
from tkinter import Tk, Frame, LEFT, RIGHT

class App:
    def getApp():
        root = Tk()
        root.title('Mortgage Calculator')
#        mortgage_frame = Frame(root, padx=8)
#        Mortgage(mortgage_frame)
#        mortgage_frame.pack(side= LEFT)
        calc_frame = Frame(root, padx= 8)
        Calculator(calc_frame)
        calc_frame.pack(side= RIGHT)
        #tp.pack()
        root.mainloop()
        