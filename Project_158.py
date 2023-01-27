# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 22:33:31 2023

@author: Akshara Sagar Dhoble
"""

from tkinter import *
from PIL import ImageTk , Image 
from tkinter import messagebox

root = Tk()
root.title("CREDIT CARD AUTHENTICATION")
root.geometry("400x400")
root.configure(background="gold")

input_box = Entry()
input_box.place(relx = 0.5 , rely=0.3 , anchor=CENTER)

img = ImageTk.PhotoImage(Image.open("Credit_card.png"))
label = Label(root , image=img)


def authentication():
    try:
        input_value = int(input_box.get())
        messagebox.showinfo("Alert" , "Credit card accepted")
        
    except(ValueError):
        messagebox.showinfo("Alert" , "Credit card not accepted . Please put valid pin code")
        
btn = Button(root , text = "Check credit card" , command= authentication)
btn.place(relx=0.5 , rely=0.4 , anchor=CENTER)
label.place(relx=0.5 , rely=0.7 , anchor=CENTER)
        
root.mainloop()
        