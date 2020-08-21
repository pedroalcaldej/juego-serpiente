import tkinter
import serpiente

root = tkinter.Tk()
root.title("la serpiente")

frame = tkinter.Frame(root)
frame.pack()
frame.config(width=500, height=200)

boton_jugar = tkinter.Button(frame, text="jugar!", command=serpiente.juego, cursor="hand2")
boton_jugar.grid(row=0, column=0, padx=150, pady=30)



root.mainloop()
