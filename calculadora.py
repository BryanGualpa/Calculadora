# calculadora.py - Versión 3:
# Corrección de requisitos: la operación principal debe ser multiplicación, no suma.
# Se mantienen: multiplicar y restar. Se muestra el problema si el usuario escribe "mas".

def calcular(operacion, a, b):
    """
    En esta versión, la calculadora realiza:
    - multiplicación (operacion = 'multiplicar')
    - resta (operacion = 'restar')
    Si se ingresa 'mas', se considera un error de operación.
    """
    if operacion == "multiplicar":
        return a * b
    elif operacion == "restar":
        return a - b
    elif operacion == "mas":
        # Aquí se evidencia el problema de requisitos: el usuario escribe 'mas'
        # pero el sistema exige 'multiplicar'.
        raise ValueError("Se ingresó 'mas', pero la operación correcta es 'multiplicar'.")
    else:
        raise ValueError("Operación no soportada. Use 'multiplicar' o 'restar'.")


if __name__ == "__main__":
    print("Calculadora - Versión 3 (multiplicar y restar)")
    print("Operaciones disponibles: multiplicar, restar")
    op = input("Ingrese la operación: ").strip().lower()
    n1 = float(input("Ingrese el primer número: "))
    n2 = float(input("Ingrese el segundo número: "))

    try:
        resultado = calcular(op, n1, n2)
        print(f"El resultado es: {resultado}")
    except ValueError as e:
        print(f"Error: {e}")
