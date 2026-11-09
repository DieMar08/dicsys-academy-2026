# %% Ejercicio 1

"""
En persona estan los datos de una persona en un diccionario: Nombre, edad, ciudad, si la cuenta esta activa y sus hobbies. 
El programa tiene que mostrar ficha
1. Imprime Nombre: Y el nombre
2. Imprime Vive en y la ciudad
3. Imprime Hobbies: y los Hobbies separados por coma
4. Si la cuenta esta activa, imprime Cuenta Activa; si no, Cuenta Inactiva
"""

# Se puede cambiar de persona
persona = {
    "nombre": "Ana",
    "Edad": 30,
    "ciudad": "Buenos Aires",
    "activo": True,
    "hobbies": ["leer", "Correr"]
}

if isinstance(persona, dict):
    hob = ""
    for act in persona["hobbies"]:
        if hob == "":
            hob += f'{act}'
        else:
            hob += f', {act}'

    print(f'Nombre: {persona["nombre"]}')
    print(f'Vive en: {persona["ciudad"]}')
    print(f'Hobbies: {hob}')

    if persona["activo"]:
        print("Cuenta activa")
    else:
        print("Cuenta inactiva")

else:
    print("Error! No es un diccionario.")
    
# %% Ejercicio 2

"""
En Datos esta el JSON de un usuario: Dentro de usuario, esta su direccion (otro diccionario) y, afuera, sus roles (una lista).
Hay que sacar datos que estan a distintas profundidades
1. Imprime el nombre del usuario
2. imprime la calle y el numer: Av. Siempre Viva 742
3. Imprime la ciudad y el pais separados por una coma: Springfield, EEUU
4. Imprime Roles: y los roles separados por coma
"""

datos = {
    "usuario": {
        "id": 123,
        "nombre": "Ana Pérez",
        "email": "ana@mail.com",
        "activo": True,
        "direccion": {
            "calle": "Av. Siempre Viva",
            "numero": 742,
            "ciudad": "Springfield",
            "pais": "EEUU",
        },
    },
    "roles": ["admin", "editor"],
    "ultimo_login": "2026-01-15",
}

print(datos["usuario"]["nombre"])
print(datos["usuario"]["direccion"]["calle"], datos["usuario"]["direccion"]["numero"])
print(datos["usuario"]["direccion"]["ciudad"] + ", " + datos["usuario"]["direccion"]["pais"])
print("Roles:", ", ".join(datos["roles"]))

# %% Ejercicio 3

"""
En texto llego un JSON, todavia como texto, con los datos de un usuario organizados en grupos.
Queremos saber que grupos tiene y que datos hay dentro de cada uno
1. Importa json, convierte texto en un diccionario con json.loads y guardalo en datos
2. Imprime Claves: y la lista de claves principales
3. Recorre las claves con un for. Si el valor de una clave es otro diccionario, imprime esa clave, dos puntos y la lista de sus claves
"""

import json

texto = """
{
  "usuario": {"nombre": "Juan Perez", "activo": true},
  "roles": ["admin", "editor"],
  "preferencias": {"idioma": "es", "tema": "oscuro"},
  "estadisticas": {
    "logins": 58,
    "ultimo_login": "2026-01-20"
  }
}
"""

datos = json.loads(texto)

print(f"Claves: {", ".join(datos.keys())}")

for clave in datos.keys():
    if isinstance(datos[clave], dict):
        print(f"{clave}: {", ".join(datos[clave].keys())}")
    else:
        print(clave)

# %% Ejerccio 4

"""
Con los datos de las variables hay que armar un diccionario, mostrarlo como JSON y guardarlos en el archivo.
1. Armar un diccionario persona con las claves nombre, edad, ciudad y activo, usando las variables
2. Importa json e imprime el diccionario como JSON con json.dumps, indent=2 y ensure_ascii=False
3. Guardalo en salida.json con json.dump
4. Para comprobar, lee el archivo con json.load e imprime Guardado: y el nombre que quedo en el archivo
"""

nombre = "Ana"
edad = 30
ciudad = "Buenos Aires"
activo = True


