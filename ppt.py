# VERSIÓN SENCILLA DEL JUEGO PIEDRA PAPEL TIJERA UTILIZANDO EL MODULO TKINTER PARA CREAR FORMULARIOS Y CONTROLES, Y EL MODULO PIL 
# PARA ABRIR Y GESTIONAR LAS IMAGENES DEL JUEGO.
# _______________________________________________________________________________________________________________________________

from tkinter import *
import os
from PIL import Image, ImageTk
import random

form = Tk()
form.geometry("530x800")
form.config(background="aliceblue")
form.resizable(False, False)
# Variable con la ubicación de los archivos donde se esta el archivo de codigo fuente 
path = os.path.dirname(os.path.realpath(__file__)) + "\\"

bg_img= ImageTk.PhotoImage(Image.open(path+"fondo.png"))
lbl_fondo = Label(form, image = bg_img) 
lbl_fondo.place(x = 0, y = 0) 

# ---------------------------------------------------------------------------------------------------------------------------------------
# Función para gestionar cada vez que se presiona un botón de piedra, papel o tijera

def jugada(jugada):  
    jugada_pc = random.choice(["piedra","papel","tijera"])
    if jugada == "tijera":
        # al presionar el botón e invocar la función, a la etiqueta lbl_jugador se le asigna la imagen correspondiente según el botón 
        # presionado.
        lbl_jugador.configure(image=img_tijera,width=150,height=200,bg="white",border=1,relief=SOLID)
        if (jugada_pc == "papel"):
            img_icono = ImageTk.PhotoImage(Image.open(path+"ganas.png"))
            lbl_icono.configure(image=img_icono)
            lbl_icono.image = img_icono
        elif (jugada_pc=="piedra"):
            img_icono = ImageTk.PhotoImage(Image.open(path+"pierdes.png"))
            lbl_icono.configure(image=img_icono)
            lbl_icono.image = img_icono
        if (jugada_pc == "tijera"):
            img_icono = ImageTk.PhotoImage(Image.open(path+"empate.png"))
            lbl_icono.configure(image=img_icono)
            lbl_icono.image = img_icono            
    elif jugada == "piedra":
        lbl_jugador.configure(image=img_piedra,width=150,height=200,bg="white",border=1,relief=SOLID)
        if (jugada_pc == "papel"):
            img_icono = ImageTk.PhotoImage(Image.open(path+"pierdes.png"))
            lbl_icono.configure(image=img_icono)
            lbl_icono.image = img_icono
        elif (jugada_pc=="piedra"):
            img_icono = ImageTk.PhotoImage(Image.open(path+"empate.png"))
            lbl_icono.configure(image=img_icono)
            lbl_icono.image = img_icono
        if (jugada_pc == "tijera"):
            img_icono = ImageTk.PhotoImage(Image.open(path+"ganas.png"))
            lbl_icono.configure(image=img_icono)
            lbl_icono.image = img_icono
    else:
        lbl_jugador.configure(image=img_papel,width=150,height=200,bg="white",border=1,relief=SOLID)   
        if (jugada_pc == "papel"):
            img_icono = ImageTk.PhotoImage(Image.open(path+"empate.png"))
            lbl_icono.configure(image=img_icono)
            lbl_icono.image = img_icono
        elif (jugada_pc=="piedra"):
            img_icono = ImageTk.PhotoImage(Image.open(path+"ganas.png"))
            lbl_icono.configure(image=img_icono)
            lbl_icono.image = img_icono
        if (jugada_pc == "tijera"):
            img_icono = ImageTk.PhotoImage(Image.open(path+"pierdes.png"))
            lbl_icono.configure(image=img_icono)
            lbl_icono.image = img_icono 
    
    # Utilizando el nombre escogido por el pc mediante el comando random.choice se abre la imagen correspondiente y se le asigna a la 
    # etiqueta lbl_pc, se utiliza la propiedad .image para que muestre la imagen, ya que solo con configure(image=) no se muestra.
    
    img_jugada_pc = ImageTk.PhotoImage(Image.open(path+jugada_pc+".jpg"))
    lbl_pc.configure(image=img_jugada_pc,width=150,height=200,bg="white",borderwidth=1,relief="solid")
    lbl_pc.image = img_jugada_pc 

# ---------------------------------------------------------------------------------------------------------------------------------------

# Creación de los controles del formulario y de las imagenes de piedra, papel, tijera que se utilizarán tanto para los botones, como para 
# las etiquetas del jugador y del pc.

img_cabecera =  ImageTk.PhotoImage(Image.open(path+"img_tit.png"))
lbl_titulo = Label(text="PIEDRA, PAPEL, TIJERA",image=img_cabecera, compound=TOP,highlightcolor="white",font=("Comic Sans MS",24,"bold"),bg="white",foreground="darkblue",border=1,relief=RAISED,padx=5,pady=5)
lbl_titulo.grid(row=0,column=0,columnspan=5,pady=15)
lbl_info = Label(text="Escoge tu jugada: ",font=("Arial",15,"bold"),foreground="white",bg="darkorange",border=1,relief=RAISED,padx=5,pady=5)
lbl_info.grid(row=1,column=0, columnspan=2,pady=15,padx=5,sticky=W)
lbl_jugador = Label()
lbl_jugador.grid(padx=5,row=6,column=0,columnspan=2,sticky=W)
lbl_pc = Label()
lbl_pc.grid(row=6,column=2,columnspan=4,sticky=W)
img_piedra = ImageTk.PhotoImage(Image.open(path+"piedra.jpg"))
img_papel = ImageTk.PhotoImage(Image.open(path+"papel.jpg"))
img_tijera = ImageTk.PhotoImage(Image.open(path+"tijera.jpg"))

# Creación de los botones para cada jugada: piedra, papel, tijera asignandoles la función jugada("") con el parametro de texto de la 
# jugada escodiga para gestionarla dentro de la función.
btn_piedra = Button(form,text="piedra",image=img_piedra,width=150,height=200,padx=45,bg="white",command= lambda: jugada("piedra"))
btn_papel = Button(form,image=img_papel,width=150,height=200,padx=45,bg="white",command= lambda: jugada("papel"))
btn_tijera = Button(form,image=img_tijera,width=150,height=200,padx=45,bg="white",command= lambda: jugada("tijera"))
btn_piedra.grid(row=2,column=0,padx=10)
btn_papel.grid(row=2,column=1,padx=10)
btn_tijera.grid(row=2,column=2,padx=10)

lbl_resultado = Label(text="Resultado: ",font=("Arial",15,"bold"),foreground="white", bg="darkorange",border=1,relief=RAISED,padx=5,pady=5)
lbl_resultado.grid(row=3,columnspan=3,pady=10,padx=5, sticky=W)

# Etiqueta para mostrar imagen indicando si se ha ganado, perdido o es un empate.
lbl_icono = Label()
lbl_icono.grid(row=6,column=1)    

# Etiquetas para indicar que se trata del jugador o del ordenador
lbl_tit1 = Label(text="Jugador",font=("Arial",12,"bold"),foreground="white",bg="green",border=1,relief=RIDGE,padx=5,pady=5)
lbl_tit1.grid(row=5,column=0,padx=5,pady=5,sticky=W)
lbl_tit2 = Label(text="PC",font=("Arial",12,"bold"),foreground="white",bg="red",border=1,relief=RIDGE,padx=5,pady=5)
lbl_tit2.grid(row=5,column=2, pady=5,sticky=W)

form.mainloop()