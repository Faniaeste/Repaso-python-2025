"https://colab.research.google.com/drive/1NdN6ID3rMZvi3GiT8P34ctn7XdqDpssi"

"""
Operaciones aritméticas
Escribe un programa que pida dos números y que devuelva su suma, resta, producto y división.

Restricciones
Convertir las cadenas de entrada en números
Separar convenientemente la entrada, transformación de cadena en números y salida separados
Crea una única sentencia de salida con los saltos de línea adecuados (sólo un print)

Retos
Controla que las entradas sean números de forma que el programa no avance si no se introduce un número
No permitas introducir números negativos
"""
seguir = True
while seguir:

    #Entrada
    numero1 = input("ingrese el primer número: ")
    numero2 = input("ingrese el segundo número: ")
    operacion = input("Ingrese la operación: +, -, * , /")

    #control
    """
    #Primera prueba y no nos sale, hasta que descubrimos isnumeric.
    while float(numero1) < 0 or float(numero2) < 0:
    print("No puedes ingresar numeros negativos, porfavor vuelve a introducirlos")
    numero1 = input("ingrese el primer número: ")
    numero2 = input("ingrese el segundo número: ")
    """


    while operacion not in "+, -, * , /":
        print("Debe ingresar operacion valida, porfavor vuelva a ingresar la operación")
        operacion = input("Ingrese la operación: +, -, * , /")

    while not(numero1.isnumeric()) or not (numero2.isnumeric) :
        print("No puedes ingresar numeros negativos, porfavor vuelve a introducirlos")
        numero1 = input("ingrese el primer número: ")
        numero2 = input("ingrese el segundo número: ")


    #Tranformación
    numero1 = float(numero1)
    numero2 = float(numero2)
    suma = numero1 + numero2
    resta = numero1 - numero2
    producto = numero1 * numero2
    division = numero1 / numero2

    #Salida~
    resultado = 0
    if operacion == '+':
        resultado = numero1 + numero2
    elif operacion == '-':
        resultado = numero1 - numero2
    elif operacion == '*':
     resultado = numero1 * numero2
    elif operacion == '/':
        resultado = numero1 / numero2
    print(f"{numero1} {operacion} {numero2} = {resultado}")

    continuar = input("Desea seguir utilizando la calculadora? s/n")
    if continuar == "n":
        seguir = False
        print("Fin de la operación")
        #break
        #print(f"La suma es: {suma}\nLa resta es: {resta}\nEl producto es: {producto}\nLa division es:  {division}")
