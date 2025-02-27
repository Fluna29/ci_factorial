"""
Este módulo contiene la función factorial(n) que calcula el factorial de un número entero n.
"""
def factorial(n):

    """
    Esta función calcula el factorial de un número entero n.
    Para ello, comprueba que sea un número entero y que sea positivo.
    Y en el caso de ser 0, devuelve 1.
    :param n:
    :return:
    """
    if not isinstance(n, int):
        raise TypeError("Input debe de ser un Integer")
    if n < 0:
        raise ValueError("No se puede hacer el factorial de un número negativo")
    if n == 0:
        return 1

    return n * factorial(n - 1)
