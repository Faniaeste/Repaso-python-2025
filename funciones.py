#Función clásica sin retorno
def saludar():
    #bloque de código que pertenece a la función saludar
    print('Hola')

#invocación de función con python siempre con los paréntesis, no hay límite
saludar()

#Las palabras reservadas de python no se pueden usar como variable.
def ver_numero():
    return 150

a = 10; b = 5; c = a + b #Se pueden declarar variables con el ; como si fuera el punto y aparte.

suma = c + ver_numero()

#print ('La suma es: ' + suma) #Aquí esta sumando una cadena y un entero, entonces petaría.

#una solución sería cambiar el signo de + por una , .
"""
print ('La suma es: ', suma)
"""
#otra solución sería converit el número a str
"""
print ('La suma es: ' + str(suma))
"""
saludo = "Hola como vas"
#funcion con parametro de entrada
def saludo_custom(saludo):
    print(saludo)
#los parametros de entrada que declaremos solo pertenecen a la funcion
#solo se pueden utilizar dentro de la funcion

saludo_custom(1000)

def datos_clientes(nombre, apellido, email, telefono):
    #pass lo que hace es que exista sin definirse, que es lo que va hacer eso.
    dato_cliente = f"Nombre: {nombre}\n, Apellido: {apellido}\n, Email: {email}\n, Telefono: {telefono}"
    print(dato_cliente)

    #La "f" te suma str o algun valor, te concatena

datos_clientes("Estefanía", "Sánchez", "faniaeste92@gmail.com", "650878262")
#si quiero que me lo imprima una debajo del otro, para hecr un salto de línea \n

def calcular_cuadrado(num):
    return num * num
print(calcular_cuadrado(5))

#controlar errores en python cualquier error

try:
    print(calcular_cuadrado('skjklsdhjksdfkj'))
except Exception as e:
    print('Ingrese un numero válido')

#el try: es una condicional, y si falla te tiene que salir el error que tu as puesto.
#esto sirve para controlar error que ya sabes que van a salir.
#por ejemplo si solo pedimos numeros, y le ponen letras, ya que salte ese error.


