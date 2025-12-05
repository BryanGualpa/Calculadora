# calculadora.py - Versión 1: solo suma

def calcular(operacion, a, b):
    """
    En esta primera versión, la calculadora solo realiza suma.
    """
    if operacion == "suma":
        return a + b
    else:
        # En esta versión no se manejan otras operaciones
        raise ValueError("Operación no soportada en esta versión.")


if __name__ == "__main__":
    print("Calculadora - Versión 1 (solo suma)")
    op = input("Ingrese la operación (suma): ").strip().lower()
    n1 = float(input("Ingrese el primer número: "))
    n2 = float(input("Ingrese el segundo número: "))

    try:
        resultado = calcular(op, n1, n2)
        print(f"El resultado es: {resultado}")
    except ValueError as e:
        print(f"Error: {e}")
