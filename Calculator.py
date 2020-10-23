# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 04:26:12 2020

@author: navee
"""
from tkinter import Frame, Label, Button, Entry, TOP, BOTTOM, RAISED

class Calculator(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        ent = Entry(master, width=38)
        ent.pack(side=TOP)
        btn_frame = Frame(master, pady= 8)
        btn_frame.pack(side=BOTTOM)
        labels = [['MC','M+','M-','MR'],
                  ['C','\u221a','x\u00b2','+'],
                  ['7','8','9','-'],
                  ['4','5','6','*'],
                  ['1','2','3','/'],
                  ['0','.','+-','=']]
        for r in range(6):
            for c in range(4):
                button = Button(btn_frame, text=labels[r][c], height=1, width=7)
                button.grid(row=r, column=c)

        