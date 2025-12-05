# calculadora.py - Versión 2: suma y resta

def calcular(operacion, a, b):
    """
    En esta versión, la calculadora puede realizar suma y resta.
    """
    if operacion == "suma":
        return a + b
    elif operacion == "resta":
        return a - b
    else:
        raise ValueError("Operación no soportada en esta versión (use 'suma' o 'resta').")


if __name__ == "__main__":
    print("Calculadora - Versión 2 (suma y resta)")
    print("Operaciones disponibles: suma, resta")
    op = input("Ingrese la operación: ").strip().lower()
    n1 = float(input("Ingrese el primer número: "))
    n2 = float(input("Ingrese el segundo número: "))

    try:
        resultado = calcular(op, n1, n2)
        print(f"El resultado es: {resultado}")
    except ValueError as e:
        print(f"Error: {e}")
