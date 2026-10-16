import tkinter



ventana = tkinter.Tk()
ventana.geometry("1200x900")

text_box = tkinter.Entry(ventana)
text_box.pack()

etiqueta = tkinter.Label(ventana)
etiqueta.pack()

def text():
    texto1 = text_box.get()
    print(texto1)
    etiqueta["text"] = texto1


button = tkinter.Button(ventana, text = "enviar", command = text)
button.pack()

ventana.mainloop()