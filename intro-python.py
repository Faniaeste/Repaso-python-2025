#Comentario de una sola linea
"""
comentario 
en varias 
lineas
"""

'''
comentarios 
de varias 
lineas
'''
'''
#Salida de información
print("Hola python")

#Entrada de información
('input(Ingrese su "nombre" ')

#Entrada de información
nombre = input('ingrese su "nombre"')#un input siempre devuelve un str ""''
variable = "Su nombre es"
print(variable,nombre)

print(type(variable))


#tipos de variables en python
#str "Texto, número y caracteres", "con comillas 'dobles'",'con comillas "simples"'
#int 100"numeros enteros"
#float 10.00 "numeros con decimales"
#bool True False

#sensible a mayúsculas y minusculas lo detecta como otra variable diferente
#las variables son muy flexibles
NAME = "Estefanía"
print(NAME)
NAME = True
print(NAME)
NAME = 100
print(NAME)
'''
#Reglas de nombres de variables
#NOMBRES DE VARIABLES Y FUNCIONES VAN EN MINISCULAS
#nombre de clases va con la primera letra en mayúsculas
#nombre de variables de tipo constante va todo en mayúsculas

#no se puede
#100names = "Jose" #números delante del nombre de la variable
# cuenta bancaria = 2343537 #Espacios entre nombre de variables

#se puede
#nombre987 = "Jose"
#se recomienda utilización de estilos de declaración de snake case y camel case
#snake case  cuenta_bancaria_personal "los guiones bajos"
#camel case CuentaBancariaPersonal "La primera letra en mayússculas"


numero1 = "100"
numero2 = 50

suma = numero2 + int(numero1)

print("La suma es: ",suma)

#no se puede sumar una cadena de texto con un entero
#casteo o casting--> tranformar una variable a otra


