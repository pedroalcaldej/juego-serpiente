import tkinter
import serpiente

root = tkinter.Tk()
root.title("la serpiente")

frame = tkinter.Frame(root)
frame.pack()
frame.config(width=500, height=200)


nombre_usuario = tkinter.StringVar()
nombre_usuario.set('')


#  MENÚ-------------------------------------------------------------------------
menu_juego = tkinter.Menu(frame)
root.config(menu=menu_juego)

configuracion = tkinter.Menu(menu_juego, tearoff=0)
configuracion.add_command(label='velocidad')
configuracion.add_command(label='obstaculos')
configuracion.add_command(label='porte de los puntos')

jugador = tkinter.Menu(menu_juego, tearoff=0)
jugador.add_command(label='cambiar jugador')

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
usuario = tkinter.Label(frame, text='Nombre de usuario')
usuario.grid(row=0, column=0, padx=10, pady=10)

usuario_input = tkinter.Entry(frame, textvariable=nombre_usuario)
usuario_input.grid(row=0, column=1, padx=10, pady=10)



boton_jugar = tkinter.Button(frame, text="jugar!", command=serpiente.juego, cursor="hand2")
boton_jugar.grid(row=2, column=1, padx=10, pady=10)



root.mainloop()
