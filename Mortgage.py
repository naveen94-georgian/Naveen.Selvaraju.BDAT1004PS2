# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 03:34:28 2020

@author: navee
"""
from tkinter import Label, Frame, Entry, Button

class Mortgage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        lbl_amount = Label(master, text='Loan Amount:')
        lbl_amount.grid(row= 0, column=0)
        
        ent_amount = Entry(master, width=25)
        ent_amount.grid(row= 0, column=1)
        
        lbl_interest = Label(master, text='Interest Rates:', pady=4)
        lbl_interest.grid(row= 1, column=0)
        
        ent_interest = Entry(master, width=25)
        ent_interest.grid(row= 1, column=1)
        
        lbl_terms = Label(master, text='Loan Terms:', pady=4)
        lbl_terms.grid(row= 2, column=0)
        
        ent_terms = Entry(master, width=25)
        ent_terms.grid(row= 2, column=1)
        
        btn_mortgage = Button(master, text= 'Compute mortgage')
        btn_mortgage.grid(row=3, column= 0)
        
        ent_mortgage = Entry(master, width=25)
        ent_mortgage.grid(row= 3, column=1)
        
    def hello(self):
        print('hello')