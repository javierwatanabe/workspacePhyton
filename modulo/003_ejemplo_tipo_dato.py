# Ejemplo de diferentes tipos de datos en Python

# Tipo de dato: Entero (int)
numero_entero = 42
print(f"Entero: {numero_entero}, Tipo: {type(numero_entero)}")

# Tipo de dato: Flotante (float)
numero_flotante = 3.14
print(f"Flotante: {numero_flotante}, Tipo: {type(numero_flotante)}")

# Tipo de dato: Cadena (str)
cadena = "Hola, Mundo!"
print(f"Cadena: '{cadena}', Tipo: {type(cadena)}")

# Tipo de dato: Booleano (bool)
booleano = True
print(f"Booleano: {booleano}, Tipo: {type(booleano)}")

# Tipo de dato: Lista (list)
lista = [1, 2, 3, 4, 5]
print(f"Lista: {lista}, Tipo: {type(lista)}")

# Tipo de dato: Tupla (tuple)
tupla = (1, 2, 3, 4, 5)
print(f"Tupla: {tupla}, Tipo: {type(tupla)}")

# Tipo de dato: Conjunto (set)
conjunto = {1, 2, 3, 4, 5,5}
print(f"Conjunto: {conjunto}, Tipo: {type(conjunto)}")

# Tipo de dato: Diccionario (dict)
diccionario = {"clave1": "valor1", "clave2": "valor2"}
print(f"Diccionario: {diccionario}, Tipo: {type(diccionario)}")

# Tipo de dato: NoneType
ninguno = None
print(f"NoneType: {ninguno}, Tipo: {type(ninguno)}")

curso = "Phyton"
print("Estás tomando un curso de "+curso)





edad = input("Dime tu edad : ")
print(edad+edad)

# Asignar valor de variable ingresada desde input
valor = input("Ingresa una cadena")
print(f"Cadena ingresada: {valor}")
###

# Ejemplo conversion implicita
num1 = 20
num2 = 2.5
print(f"Tipos de datos iniciales de 20 y 2.5")
print(type(num1))
print(type(num2))
print(f"Tipos de datos despues de la suma de 20 y 2.5")
num1 = num1 + num2
print(type(num1))
print(type(num2))

"""
"""