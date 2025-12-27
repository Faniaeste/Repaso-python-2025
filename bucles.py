"""
#while se repite el loque de codigo mientras condición sea verdadera(True)

seguir = True
while seguir:
    print('Esto funciona')

    fin = input('Desea seguir con este whilw? s/n')
    if fin== "n":
        seguir = False
        print("Esto se ha acabado")
        
#while con else
nombre = "María"
while nombre == "Jose":
    print("Hola", nombre)
else:
    print("No es María")

#imprimir valores del 1 al 100
cont = 0
while cont < 100:
    cont = cont + 1
    print(cont)
#el contador + 1, hay que ponerlo enima del print, hay que sumarlo antes de imprimirlo.
# o solución dos, poner el contador en lugar de = 0 , ponerlo a = 1.
"""




"""
#Bucle for, se repite mientras se cumpla el número de iteraciones(repeticones) definidas.
#Metodo dentro del for range(inicio, final(el número dado -1), salto(Opcional))
#imprimir valores del 1 al 100
for iteracion in range(1,101):
    print(iteracion)
#si quieres que empiece desde 0, cambias el 1 por el 0.
#Realizar un programa que muestre la tabla de multiplicar dado un número.


numero = input("Introduce un numero: ")
numero = int(numero)
for i in range(1,11):
    print(f"{numero} x {i} = {numero * i}")
#Todo lo que entra por input es en str, aunque indroduzcas números,
#No los suma ni los multiplica, los concatenan.
#en una sola linea se podria hacer así.
#numero = int(input("Introduce un numero: "))
"""


#Esto es lo mismo, metiendolo en una función, he cambiado el input de lugar.
#porque si lo dejo donde estaba anteriormente, me pide que introduzca el número.
#2 veces al llamar a la función
def tabla_de_multiplicar(numero):
    numero = int(numero)
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")

seguir_multipicando = True

while seguir_multipicando:
    num = input("Introduce un numero: ")
    tabla_de_multiplicar(num)

    valor = input("Desea seguir con la tabla? s/n")

    if valor == "n":
        seguir_multipicando = False
        print("Programa finalizado")


