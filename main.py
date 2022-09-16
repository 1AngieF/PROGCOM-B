# Programa que calcule la derivada y la integral de una función

import os
os.system('pip install pyargs chempy')
os.system('pip install sympy')

from sympy import *
from sympy.parsing.sympy_parser import parse_expr  # Leer función introducida
from tkinter import *
from chempy import balance_stoichiometry


def reactivos():
    try:
        reactivos_escrita = reactivos.get()
        productos_escrita = productos.get()
        resultado = balance_stoichiometry({reactivos_escrita}, {productos_escrita})
        etiqueta.configure(text="resultado")

    except:
        etiqueta.configure(text="Introduce la función correctamente")


ventana = Tk()
ventana.geometry('400x280')
ventana.title("Balance de ecuaciones químicas")

anuncio = Label(ventana, text="Introduce los reactivos", font=("Arial", 15), fg="blue")
anuncio.pack()

reactivos = Entry(ventana, font=("Arial", 15))
reactivos.pack()

anuncio = Label(ventana, text="Introduce los productos", font=("Arial", 15), fg="blue")
anuncio.pack()

productos = Entry(ventana, font=("Arial", 15))
productos.pack()

etiqueta = Label(ventana, text="Resultado", font=("Arial", 15), fg="red")
etiqueta.pack()

boton1 = Button(ventana, text="Balancear", font=("Arial", 15), command='resultado')
boton1.pack()


def _quit():  # Función salir
    ventana.quit()  # detiene mainloop
    ventana.destroy()  # elimina la ventana de la memoria


button3 = Button(master=ventana, text="Salir", font=("Arial", 15), command=_quit)
button3.pack()

ventana.mainloop()



ANGIE MICHELLE GONZALEZ FERNANDEZ
LOS CODIGOS Y LIBRERIAS SE COGIERON DE https://youtu.be/Ebmw-iHPb2w