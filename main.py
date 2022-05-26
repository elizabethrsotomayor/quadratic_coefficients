def quadratic_coefficients(x1: int, x2: int) -> tuple:
    """
    Find the coefficients of quadratic equation of the given two roots.
    Equation will be the form of ax^2 + bx + c = 0
    :param x1: First root
    :param x2: Second root
    :return: tuple containing values (a, b, c)
    """
    a = 1
    b = -(x1 + x2)
    c = x1 * x2
    return a, b, c
