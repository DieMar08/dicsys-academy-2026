# 2. Un cine hace descuento a menores de 12 años, a mayores de 65 y a cualquier persona los miercoles. Dadas edad y es_miercoles
# (True o False), imprime Con descuento o Precio Normal

edad = 40
es_miercoles = True

if edad < 12 or edad > 65 or not es_miercoles:
    print("con descuento")
else:
    print("precio normal")

# 3. Dado un numero, imprime su tabla de multiplicar del 1 al 10, un resultado por linea, con el formato 7 x 3 = 21

numero = 3

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# Como dato extra, solo imprimir los resultados pares

numero = 3

for i in range(1, 11):
    if numero * i % 2 == 0:
        print(f"{numero} x {i} = {numero * i}")

# 4. Dada la lista ventas con los montos del dia, imprime el total y el promedio de 2 lineas: Total: 1250 y Promedio: 250.0.
# Hazlo con un for, sin usar sum ()

ventas = (200, 350, 100, 400, 200)
total = 0

for i in ventas:
    total += i

print("Total:", total)
print("Promedio", total/len(ventas))

# Y que pasa si no hay ventas?

ventas = []
total = 0

if not ventas:
    print("Sin ventas")
else:
    for i in ventas:
        total += i

    print("total:", total)
    print("Promedio", total / len(ventas))
    
# 5. Un sensor envia lecturas y marca el fin de los datos con un -1 con un while, suma las lecturas que hay antes del -1
# (sin incluirlo) e imprime en 2 lineas cuantas son y su suma: Lecturas: 3 y Suma: 36
# Lecturas = [12, 15, 9, -1, 20, 7]

lecturas = [12, 15, 9, -1, 20, 7]

i = 0
suma = 0

while lecturas[i] != -1:
    suma += lecturas[i]
    i += 1

print(f"Lecturas: {i}")
print(f"Suma: {suma}")

# 6. Partiendo de compras: 1) Agrega "pan" al final; 2) Quita "leche" si esta; 3) Si "huevos" no esta, agregalo. Al final imprime
# la lista y, en otra linea, la cantidad con el formato total: 4 productos

compras = ["leche","arroz","cafe"]
compras.append("pan")

if "leche" in compras:
    compras.remove("leche")

if "huevos" not in compras:
    compras.append("huevos")

print(compras)
print(f"Total: {len(compras)} productos")

# La lista emails llego de un formulario con espacios y mayusculas. Crea una lista nueva, limpios, con cada email sin espacios
# en los bordes y minusculas, e imprimelas

