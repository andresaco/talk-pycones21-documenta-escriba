
def sum(a: int, b: int) -> int:
    """
    Let's sum two integers!

    >>> sum(1,2)
    3

    :param a: An integer
    :param b: Another integer

    :return: the sum of both parameters

    """
    return a + b


def sub(a: int, b: int) -> int:
    """
    Substract b to a

    >>> sub(10, 2)
    8

    :param a: An integer
    :param b: Another integer

    :return: the result of substracting b to a

    """
    return a - b


def mul(a: int, b: int) -> int:
    """
    Get b times a

    >>> mul(3, 2)
    6

    :param a: An integer
    :param b: Another integer

    :return: b times a

    """
    return a * b


def div(a: int, b: int) -> float:
    """
    Division, mind the zero!

    >>> div(10, 2)
    5.0

    :param a: An integer
    :param b: Another integer

    :return: the result of dividing a and b

    :raises:
        ZeroDivisionError: if parameter b is 0

    """
    return a / b
