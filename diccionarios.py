# Un diccionario, Es un contenedor de Python
personas = {"nombre":"Rosa", "edad":65, "ciudad":"Extremadura"}

print(len(personas))
print(personas["edad"])#65
print(personas["nombre"])#Rosa
print(personas["ciudad"])#Extremadura

personas["nombre"] = "Jose"
print(personas["nombre"])

print(personas.keys())#obtengo todas las claves o keys
print(personas.values())#obtener todos los valores
print(personas.items())#obtener valor y claves
print(personas.get("ciudad"))#sirve para hacer una busqueda de un valor por su key; sino existe devielve none, 
print(personas.pop("edad"))#elimina un elemento por su clave
print(personas.update({"país":"España"}))#añade un elemento nuevo
print(personas)

for k,v in personas.items():
    print(f"key: {k}, value: {v}")