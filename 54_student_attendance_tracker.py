lista_de_estudiantes = {}

while True:
    name_estudiante = input("inserte el nombre del estudiante:")

    if name_estudiante== "0":
        break

    presente = input("el estudiante esta presente?:")

    lista_de_estudiantes.update({name_estudiante: presente})

for estudiante, presente in lista_de_estudiantes.items():
    print(f"{estudiante}: {presente}")
print(lista_de_estudiantes)