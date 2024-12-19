import math

# Ejemplo completo con varias operaciones matemáticas
a = 15
b = 4

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
exponenciacion = a ** b
modulo = a % b
division_entera = a // b
log_natural = math.log(a)
log_base_10 = math.log10(a)
seno = math.sin(math.radians(30))  # Convertir grados a radianes
coseno = math.cos(math.radians(60))  # Convertir grados a radianes

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
print(f"Exponenciación: {exponenciacion}")
print(f"Módulo: {modulo}")
print(f"División entera: {division_entera}")
print(f"Logaritmo natural de {a}: {log_natural}")
print(f"Logaritmo base 10 de {a}: {log_base_10}")
print(f"Seno de 30 grados: {seno}")
print(f"Coseno de 60 grados: {coseno}")

# Mostrar parte entera de una raiz cuadrada
numero = 783
raiz =int(numero**0.5)
print(raiz)
