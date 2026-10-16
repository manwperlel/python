import tkinter

ventana = tkinter.Tk()
ventana.geometry("1200x900")

button1 = tkinter.Button(ventana, text = "boton1", width = 10, height = 5)
button2 = tkinter.Button(ventana, text = "boton2", width = 10, height = 5)
button3 = tkinter.Button(ventana, text = "boton3", width =10, height = 5)

button1.grid(row = 0, column = 1 )
button2.grid(row = 1, column = 2 )
button3.grid(row = 2, column = 3 )


ventana.mainloop()