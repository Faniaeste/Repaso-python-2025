'https://colab.research.google.com/drive/11L8qDxtCPFtHwuSs1Mh8VE3hS4RUdbg6'
'''
Hola, mundo
Hacer un programa que pida el nombre y te salude por tu nombre

Restricciones
Mantener entrada, salida y concatenación separados


Retos
Escribir el programa sin usar variables
Escribir un programa que devuelva diferentes tipos de saludos a diferentes tipos de persona.
'''
'''
def entrada():
    #Entrada
    nombre = input("Escribe tu nombre: ")
    return nombre
def concatenacion(nombre):
    #concatenación
    saludo = "Hola " + nombre
    return saludo
def salida(saludo):
    #Salida
    print(saludo)
'''
'''
nom = entrada()
mensaje = concatenacion(nom)
salida(mensaje)

persona1 = "Jose"
persona2 = "Ricardo"
persona3 = "Ruth"

saludo1 = "Hola"
saludo2 = "Hello"
saludo3 = "Ciao"

'''

#Reto 1
print("Hola "+input("Ingrese el nombre: "))

#Reto 2
personasLista = ["Jose","Ricardo","Ruth"]
saludoLista = ["Hola ","Hello ","Ciao "]

"""
print(saludoLista[0]+personasLista[0])
print(saludoLista[1]+personasLista[1])
print(saludoLista[2]+personasLista[2])
"""

for i in range(3):
    print(saludoLista[i]+personasLista[i])



