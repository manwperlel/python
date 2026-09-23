print("===========================  GESTOR DE LIBRERIA  ===================================\n\n\n")



print("ingrese 1 para agregar un nuevo libro")
print("ingrese 2 para quitar el ultimo libro agregado")
print("ingrese 3 para quitar un libro en especifico")
print("ingrese 4 para mostrar un libro en especifico")
print("ingrese 5 para mostrar toda la libreria\n")


print("ingrese C para limpiar toda la libreria\n\n")

interacion = input("ingrese un numero:").strip().lower()
library = [
{"id": 1, "autor":"autor1", "año": 1984, "genero":"terror"},
{"id": 2, "autor":"autor2", "año": 2010, "genero":"amor"},
{"id": 3, "autor":"autor3", "año": 1961, "genero":"poesia"}
]



if interacion == "1":
    titulo = input("ingrese un nombre del nuevo libro:")
"""elif interacion == "2":
    titulo = input("ingrese el libro que desea quitar:")
elif interacion == "3":
    titulo = input("ingrese el libro que desea quitar:")
elif interacion == "4":
    titulo = input("ingrese el libro que desea revisar:")
elif interacion == "5":
    for i in library:
        print(i)
elif interacion == "c":
    library.clear()
    print(library)
else:
    interacion = input("ingrese un numero:")"""