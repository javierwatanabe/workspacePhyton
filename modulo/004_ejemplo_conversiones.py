
# Convertir float a entero 
num1 = 7.5
temporal = int(num1)
print(temporal)

# Convertir float a entero y mostrar tipo de dato
num1 = 7.5
num1 = int(num1)
print(type(num1))


# Convertir entero a float y mostrar tipo de dato
num1 = 10
num1 = float(num1)
print(type(num1))

# Suma de numero int y float
num1 = "7.5"
num2 = "10"
print(float(num1) + int(num2))
print(f"La suma de {num1} y {num2} es {float(num1) + int(num2)}")

print("1. Conversión de Entero a Flotante **************")
numero_entero = 5
numero_flotante = float(numero_entero)
print(f"Entero: {numero_entero}, Flotante: {numero_flotante}")

print("2. Conversión de Flotante a Entero **************")
numero_flotante = 5.8
numero_entero = int(numero_flotante)
print(f"Flotante: {numero_flotante}, Entero: {numero_entero}")

print("3. Conversión de Entero a Cadena **************")
numero_entero = 42
cadena = str(numero_entero)
print(f"Entero: {numero_entero}, Cadena: '{cadena}'")
print("4. Conversión de Cadena a Entero **************")

cadena = "123"
numero_entero = int(cadena)
print(f"Cadena: '{cadena}', Entero: {numero_entero}")

print("5. Conversión de Cadena a Flotante **************")
cadena = "3.14"
numero_flotante = float(cadena)
print(f"Cadena: '{cadena}', Flotante: {numero_flotante}")

print("6. Conversión de Entero a Booleano **************")
numero_entero = 0
booleano = bool(numero_entero)
print(f"Entero: {numero_entero}, Booleano: {booleano}")

numero_entero = 1
booleano = bool(numero_entero)
print(f"Entero: {numero_entero}, Booleano: {booleano}")

print("7. Conversión de Cadena a Lista de Caracteres **************")
cadena = "Hola"
lista = list(cadena)
print(f"Cadena: '{cadena}', Lista: {lista}")

print("8. Conversión de Lista a Cadena **************")
lista = ['H', 'o', 'l', 'a']
cadena = ''.join(lista)
print(f"Lista: {lista}, Cadena: '{cadena}'")

print("9. Conversión de Diccionario a Lista de Claves **************")
diccionario = {"clave1": "valor1", "clave2": "valor2"}
claves = list(diccionario.keys())
print(f"Diccionario: {diccionario}, Claves: {claves}")

print("10. Conversión de Diccionario a Lista de Valores **************")
diccionario = {"clave1": "valor1", "clave2": "valor2"}
valores = list(diccionario.values())
print(f"Diccionario: {diccionario}, Valores: {valores}")
