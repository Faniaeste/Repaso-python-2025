#Operadores lógicos
#(==) - igual, (!=) - diferente de, (<) - más pequeño que, (>) - má grande que.
a = 10
b = 5
print(a == b)#False
print(a < b)#False
print(a > b)#True
print(a != b)#True

#Condicional if clásica, suelen ser para números.
#Para str solo se usa (==) o (!=), porque lo que compara son la cantidad de carácteres.
"""if a > 5:
    print('a es mayor a 5')"""
#Condicional if con else
a = 'María'
if a == 'María':
    print('Es María')

else:
    print('No es María')

#Condicional con if elif, esto e una condicional anidada.
dia = 'Jueves'

if dia == 'Martes':
    print('Hoy es Martes')
elif dia == 'Miercoles':
    print('Hoy es Miércoles')
elif dia == 'Jueves':
    print('Hoy es Jueves')
else:
    print('No es ningún dia requerido')
#No hay limites de elif, siempre y cuando sea sobre la misma variable
#Operadores de unión and(y), or(o) y not(Este lo que hace es negar toda una condición)
nombre = 'Jose'
password = 'jose123'

if nombre == 'Jose' and password == 'jose123':
    print('bienvenido al sistema')
else:
    print('Tu contrasña o usuario es incorrecto')
