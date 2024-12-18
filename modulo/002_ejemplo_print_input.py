import math

# Ejemplo de uso de las funciones print e input

print("Mi ejemplo---------------")
print(input("¿En que pais vives?"))
print("Saludar al Usuario---------------")
nombre = input("¿Cuál es tu nombre? ")
print(f"Hola, {nombre}! Encantado de conocerte.")

print("Suma de Dos Números---------------")
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
suma = numero1 + numero2
print(f"La suma de {numero1} y {numero2} es {suma}.")

print("Convertir Grados Celsius a Fahrenheit---------------")
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")

print("Calcular el Área de un Círculo---------------")
radio = float(input("Ingresa el radio del círculo: "))
area = math.pi * (radio ** 2)
print(f"El área del círculo con radio {radio} es {area}.")

print("Jugar con Strings---------------")
frase = input("Ingresa una frase: ")
longitud = len(frase)
print(f"La frase '{frase}' tiene {longitud} caracteres.")

print("Verificar la Edad para Permitir Acceso---------------")
edad = int(input("¿Cuántos años tienes? "))
if edad >= 18:
    print("Eres mayor de edad. Puedes acceder.")
else:
    print("Lo siento, eres menor de edad. No puedes acceder.")

print("Ejemplo concatenacion---------------")
print(f"Hola, {input('Ingresa tu nombre: ')} {input('Ingresa tu apellido: ')}!")

print("Ejemplo operador %---------------")
nombre = "Charlie"
edad = 25
print("Hola, %s. Tienes %d años." % (nombre, edad))

print("Ejemplo metodo format ---------------")
nombre = "Brown"
edad = 28
print("Hola, {}. Tienes {} años.".format(nombre, edad))

pi = 3.14159
print("El valor de pi es aproximadamente {:.2f}".format(pi))

print("Ejemplo de Unformatted String---------------")
mensaje = "Hola, Mundo!"
print(mensaje)  # Simplemente imprime la cadena literal

print("Ejemplo de Udemy ---------------")
print("Tu nombre es "+ input("Dime tu nombre: ")+ " " +input("Dime tu apellido: :"))


print(input("¿Qué estás estudiando?"))

print("Tu nombre y apellido son:  "+ input("Escribe tu nombre: ")+ " " +input("Escribe tu apellido: :"))

nombre = input("Escribe tu nombre: ")
apellido = input("Escribe tu apellido: ")
print(f"{nombre} {apellido}")


print("El nombre de tu cerveza\nes\t \"" + input("¿Cual es tu día favorito de la semana: ") + " " + input("¿Cual es tú número preferido de 3 dígitos?: ") + "\".\n¡Felicitaciones!")
