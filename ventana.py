import tkinter
from tkinter import messagebox
from tkinter import ttk
import serpiente
import sqlite3

root = tkinter.Tk()
root.geometry('300x100')
root.title('la serpiente')

frame = tkinter.Frame(root)
frame.pack()

# Variables---------------------------------------------------------------------
nombre_usuario = tkinter.StringVar()
nombre_usuario.set('')
texto_contraseña = tkinter.StringVar()
texto_contraseña.set('')
sesion = False

# Funciones---------------------------------------------------------------------
def inicio_sesion():
    conexion = sqlite3.connect('datos usuarios')
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO DatosUsuarios (Usuario, Contraseña) VALUES ('{}', '{}')".format(nombre_usuario.get(), texto_contraseña.get()))
    conexion.commit()
    global sesion
    sesion = True
    root.title('a serpiente - ' + nombre_usuario.get())
    messagebox.showinfo('Sesión iniciada', 'Juega nomás. Besos en el potito')
    conexion.close()

def iniciar_sesion():
    usuario = tkinter.Label(frame, text='Nombre de usuario')
    usuario.grid(row=0, column=0, padx=5, pady=5)
    usuario_input = tkinter.Entry(frame, textvariable=nombre_usuario)
    usuario_input.grid(row=0, column=1, padx=5, pady=5)
    contraseña = tkinter.Label(frame, text='Contraseña')
    contraseña.grid(row=1, column=0, padx=5, pady=5)
    contraseña_input = tkinter.Entry(frame, textvariable=texto_contraseña)
    contraseña_input.grid(row=1, column=1, padx=5, pady=5)
    boton_guardar = tkinter.Button(frame, text='Guardar usuario', command=inicio_sesion)
    boton_guardar.grid(row=2, column=0, padx=5, pady=5)

def jugar():
    if sesion:
        serpiente.juego()
    else:
        messagebox.showinfo('Avíspate', 'Inicia sesión para poder jugar')
        iniciar_sesion()


#  MENÚ-------------------------------------------------------------------------
menu_juego = tkinter.Menu(frame)
root.config(menu=menu_juego)

configuracion = tkinter.Menu(menu_juego, tearoff=0)
configuracion.add_command(label='velocidad')
configuracion.add_command(label='obstaculos')
configuracion.add_command(label='porte de los puntos')

jugador = tkinter.Menu(menu_juego, tearoff=0)
if sesion:
    accion_sesion = 'Cerrar sesión'
else:
    jugador.add_command(label='Iniciar sesión', command=iniciar_sesion)

vista = tkinter.Menu(menu_juego, tearoff=0)
vista.add_command(label='claro')
vista.add_command(label='oscuro')

salir = tkinter.Menu(menu_juego, tearoff=0)
salir.add_command(label='cambiar de juego')
salir.add_command(label='salir')

menu_juego.add_cascade(label='configuracion', menu=configuracion)
menu_juego.add_cascade(label='jugador', menu=jugador)
menu_juego.add_cascade(label='vista', menu=vista)
menu_juego.add_cascade(label='salir', menu=salir)


# WIDGETS-----------------------------------------------------------------------
boton = tkinter.Button(frame, text='Jugar!', command=jugar, cursor="hand2")
boton.grid(row=2, column=1, padx=10, pady=10)


root.mainloop()
