# Almacena el número de estudiantes a ingresar
cantidad = int(input("Cuantos estudiantes desea ingresar: "))

# Esta lista almacena los resultados académicos
resultados = []

for i in range(cantidad):
    print('Ingresa datos del estudiante: ')
    nombre = input("Ingresa el nombre del estudiante {0}°\n".format(i+1))
    notas = []

    for j in range(3):
        nota = float(input("Ingresa la nota {0}\n".format(j+1)))
        notas.append(nota)

    resultados.append([nombre, notas])

print("-" * 55)
print("Nombre".ljust(15) + "| Nota 1".ljust(15) + "| Nota 2".ljust(15) + "| Nota 3".ljust(15) + "| Promedio".ljust(15))
print("-" * 55)

for estudiante in resultados:
    nombre, notas = estudiante
    promedio = round(sum(notas) / len(notas), 2)
    print(nombre.ljust(15), end="| ")
    for nota in notas:
        print(str(nota).ljust(15), end="| ")
    print(str(promedio).ljust(15))

