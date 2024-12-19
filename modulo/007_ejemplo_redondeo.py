valor= round(1974.123456789987654321,2)
print(valor)
print(type(valor))

valor1= 1975.1234567899876543212
print(round(valor1))
print(type(valor1))

valor2= round(1975.1234567899876543212)
print(valor2)
print(type(valor2))


import math
from decimal import Decimal, ROUND_HALF_UP, ROUND_DOWN, ROUND_UP

def ejemplos_redondeo():
    # Número a utilizar en los ejemplos
    numero = 3.567
    numero_negativo = -3.567

    # Usando round() al entero más cercano
    redondeado_round = round(numero)
    print(f"{numero} redondeado al entero más cercano es {redondeado_round}")

    # Usando round() a 2 decimales
    redondeado_round_decimales = round(numero, 2)
    print(f"{numero} redondeado a 2 decimales es {redondeado_round_decimales}")

    # Usando math.floor() para redondear hacia abajo
    redondeado_floor = math.floor(numero)
    print(f"{numero} redondeado hacia abajo es {redondeado_floor}")

    # Usando math.ceil() para redondear hacia arriba
    redondeado_ceil = math.ceil(numero)
    print(f"{numero} redondeado hacia arriba es {redondeado_ceil}")

    # Usando math.floor() para número negativo
    redondeado_floor_negativo = math.floor(numero_negativo)
    print(f"{numero_negativo} redondeado hacia abajo es {redondeado_floor_negativo}")

    # Usando math.ceil() para número negativo
    redondeado_ceil_negativo = math.ceil(numero_negativo)
    print(f"{numero_negativo} redondeado hacia arriba es {redondeado_ceil_negativo}")

    # Usando decimal.Decimal y quantize para redondeo con precisión
    numero_decimal = Decimal('3.567')
    redondeado_decimal_half_up = numero_decimal.quantize(Decimal('1.00'), rounding=ROUND_HALF_UP)
    print(f"{numero_decimal} redondeado a 2 decimales (ROUND_HALF_UP) es {redondeado_decimal_half_up}")

    # Redondeo hacia abajo usando decimal
    redondeado_decimal_down = numero_decimal.quantize(Decimal('1'), rounding=ROUND_DOWN)
    print(f"{numero_decimal} redondeado hacia abajo (ROUND_DOWN) es {redondeado_decimal_down}")

    # Redondeo hacia arriba usando decimal
    redondeado_decimal_up = numero_decimal.quantize(Decimal('1'), rounding=ROUND_UP)
    print(f"{numero_decimal} redondeado hacia arriba (ROUND_UP) es {redondeado_decimal_up}")

if __name__ == "__main__":
    ejemplos_redondeo()
