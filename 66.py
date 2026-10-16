import tkinter

ventana = tkinter.Tk()
ventana.geometry("1200x900")

def mensaje():
    print(f"hola, soy {text_box_name.get()} {text_box_last_name.get()} tengo {text_box_age.get()} y vivo en {text_box_city.get()}")



etiqueta_nombre = tkinter.Label(ventana, text = "nombre") 
etiqueta_nombre.grid(row= 0, column= 1)

text_box_name = tkinter.Entry(ventana)
text_box_name.grid(row = 0, column = 2)

text_box_last_name = tkinter.Entry(ventana)
text_box_last_name.grid(row = 1, column = 1)

text_box_age = tkinter.Entry(ventana)
text_box_age.grid(row = 2, column = 1)

text_box_city = tkinter.Entry(ventana)
text_box_city.grid(row = 3, column = 1)

enviar = tkinter.Button(ventana, text = "enviar", command = mensaje)
enviar.grid(row = 4, column = 0)


ventana.mainloop()