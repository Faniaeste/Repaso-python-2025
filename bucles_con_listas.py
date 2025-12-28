lista_all = ["María", 10, True, 3.99,[1,2,3]]
print(len(lista_all)) #obtener la longitud de la lista
print(lista_all[0])#obteer el valor de la primera posición
print(lista_all[-1])#obtener el valor de la ultima posicion de mi lista
print(lista_all[len(lista_all)-1])#obtener el valor de la ultima posicion de mi lista

print(lista_all[0])
print(lista_all[1])
print(lista_all[2])
print(lista_all[3])
print(lista_all[4])

lista_all[0] = "Juana"
print(lista_all)

print("#lista con for")

for valores in lista_all: #Recorre los valores de la lista
    print(valores)


for iteration in range(0,len(lista_all)):#e range aquí ya hace el menos uno para coger el ultimo valor.
    if iteration == 3:
        print(lista_all[iteration])

print("#recorrer lista con while")
cont = 0
while cont < len(lista_all):
    print(lista_all[cont])
    cont = cont + 1 #o esto es equivalente cont += 1

print ("#recorrer un str con un for")

for i in "Estefanía":
    if i == "í":
        print("Existe una í" ,i)


